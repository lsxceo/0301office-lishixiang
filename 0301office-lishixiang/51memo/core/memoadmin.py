#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# memoadmin.py
# author: lishixiang

import os
import pickle
import time
from datetime import datetime
import json
from . import configadmin, log_ctrl, memo, setting, pdf_demo, mailmaster


class MemoAdmin:
    "在备忘录里实现登录，注册， 导出文件的类"
    def __init__(self):
        settings = setting.Settings()
        self.BASE_DIR = settings.BASE_DIR
        self.db_path = settings.db_path
        self.conf_path = settings.conf_path
        self.log_path = settings.log_path
        self.config_name = settings.config_name
        self.logger_name = settings.logger_name
        self.level = settings.level
        self.menu = settings.menu
        self.mail_send_choose = settings.mail_send_choose
        self.config = configadmin.ConfigAdmin(self.conf_path, self.config_name)
        self.logger = log_ctrl.common_log(self.logger_name, log_file=os.path.join(self.log_path, self.logger_name), level=self.level)
        if not os.path.exists(os.path.join(self.db_path, 'users.pkl')):
            with open(os.path.join(self.db_path, 'users.pkl'), 'wb') as f:
                pickle.dump('', f)

    def register(self):
        "注册账户"
        user = input("请输入要注册的账户名称(exit退出)：")
        if user == 'exit':
            exit()
        else:
            psd = input("请输入密码： ")
            psd_check = input("请再次输入密码： ")
            email = input("请输入email账号： ")
            if psd != psd_check:
                print('输入有误！请重新输入：')
                return self.register()
            else:
                if user in self.config.config.sections():
                    print(f'{user}已经存在，选择登录还是注册其他账号？')
                    choose = input("'y' - 返回登录界面\n'n' - 返回注册界面\n")
                    if choose == 'y':
                        return self.login()
                    else:
                        return self.register()
                else:
                    # 把账号密码写入 users.pkl 文件
                    with open(os.path.join(self.db_path, 'users.pkl'), 'rb') as f:
                        data = pickle.load(f)
                    datas = dict(data)
                    datas[user] = psd
                    with open(os.path.join(self.db_path, 'users.pkl'), 'wb') as f:
                        pickle.dump(datas, f)
                    # self.logger.warning(f"新用户'{user}'已创建")  # 添加日志文件

                # 创建用户的数据文件
                with open(os.path.join(self.db_path, user + '.pkl'), 'wb') as f:
                    pickle.dump([], f)

                # 把用户配置信息添加到配置文件
                self.config.add_config(user, 'db_path', '${base_dir}/db')
                self.config.add_config(user, 'db_type', 'pkl')
                self.config.add_config(user, 'db_name', user + '.pkl')
                self.config.add_config(user, 'email', email)
                # self.logger.info("添加新用户的配置信息")  # 添加日志文件

                # 添加到日志文件
                self.logger.warning("新用户%s已创建" % user)
                print('注册成功！')
            return self.login()

    def login(self):
        "登录账户"
        print('欢迎进入登录界面'.center(30, '*'))
        user = input("请输入账号(exit退出)： ")
        if user == 'exit':
            exit()
        else:
            if user not in self.config.config.sections():
                print('输入的账号不存在！')
                return self.register()
            else:
                psd = input("请输入密码：")
                with open(os.path.join(self.db_path, 'users.pkl'), 'rb') as f:
                    datas = pickle.load(f)
                for k, v in datas.items():
                    if k == user:
                        value = v
                        break
                if psd == value:
                    self.logger.info('验证成功！')
                    print('登录成功！')
                    return user
                else:
                    self.logger.warning('密码输入错误！')
                    return self.login()

    def choose_menu(self, user):
        "用户选择界面"
        print(f'{user.title()}欢迎进入51备忘录'.center(30, '-'))
        print('-'*30)
        for k, v in self.menu.items():
            print(f'{k}: {v}')
        try:
            choose = input('请输入要操作的菜单：')
            if choose == 'q':
                exit()
            else:
                # with open(os.path.join(self.db_path, f'{user}.pkl'), 'rb') as f:
                #     datas = pickle.load(f)
                func = getattr(self, self.menu[choose])
                func(user)
        except Exception as e:
            print(f"输入有误：错误为'{e}''")
        time.sleep(2)
        return self.choose_menu(user)

    def add(self, user):
        "增加备忘录条目"
        event = input('请输入要添加的备忘事项：(示例：明天下午2点开会@小李@小王)')
        newmemo = memo.Memo(event)
        memo_dict = newmemo.memo_dict()
        num_list = []
        with open(os.path.join(self.db_path, f'{user}.pkl'), 'rb') as f:
            datas = pickle.load(f)
        if datas == []:
            memo_dict['id'] += 1
        else:
            for dic in datas:
                id = dic['id']
                num_list.append(id)
            value = max(num_list) + 1
            newmemo.id_set = value
            memo_dict['id'] = newmemo._id
        datas.append(memo_dict)
        # print(datas)
        with open(os.path.join(self.db_path, f'{user}.pkl'), 'wb') as f:
            pickle.dump(datas, f)
        self.logger.warning(f'新增备忘条目：{newmemo}')  # 打印出添加备忘录成功的信息

    def delete(self, user):
        "删除备忘录条目"
        with open(os.path.join(self.db_path, f'{user}.pkl'), 'rb') as f:
            datas = pickle.load(f)
        for m in datas:
            mm = memo.Memo(id_=m['id'], time_=m['time_'], thing=m['thing'], name=m['name'])
            print(mm)
        id_ = input('请输入要删除的备忘事项的ID： ')
        for m in datas:
            if m['id'] == int(id_):
                del_id = int(id_)
                del_memo = f"{m['time_']} {m['thing']} {m['name']}"
                datas.remove(m)
                self.logger.warning(f'删除条目-ID: {del_id}    {del_memo}')  # 打印出删除备忘录的信息
        with open(os.path.join(self.db_path, user + '.pkl'), 'wb') as f:
            pickle.dump(datas, f)

    def modify(self, user):
        "修改备忘录条目"
        with open(os.path.join(self.db_path, f'{user}.pkl'), 'rb') as f:
            datas = pickle.load(f)
        for m in datas:
            mm = memo.Memo(id_=m['id'], time_=m['time_'], thing=m['thing'], name=m['name'])
            print(mm)
        num = int(input('请输入你要修改的备忘事项的ID： '))
        event_new = input('请输入修改后的事项： ')
        memo_new = memo.Memo(event_new)
        for m in datas:
            if m['id'] == num:
                # 修改前的备忘录
                before_memo = f"ID: {num}    {m['time_']} {m['thing']} {m['name']}"
                # 修改字典
                m['time_'] = memo_new.time_
                m['thing'] = memo_new.thing
                m['name'] = memo_new.name
                self.logger.warning(f'备忘录修改成功!  {before_memo} 修改为 {memo_new}')  # 打印出修改备忘录的信息
        with open(os.path.join(self.db_path, user + '.pkl'), 'wb') as f:
            pickle.dump(datas, f)

    def query(self, user):
        "查询备忘录条目"
        with open(os.path.join(self.db_path, f'{user}.pkl'), 'rb') as f:
            datas = pickle.load(f)
        for m in datas:
            mm = memo.Memo(id_=m['id'], time_=m['time_'], thing=m['thing'], name=m['name'])
            print(mm)
        print('- -'*15)
        self.logger.info('查看备忘录列表')

    def month_query(self, user):
        "按月份查询备忘录条目，返回JSON数据"
        print('-' * 20)
        month_query_list = []
        month = input('请输入要查询的月份：')
        with open(os.path.join(self.db_path, f'{user}.pkl'), 'rb') as f:
            datas = pickle.load(f)
        for m in datas:
            mon = datetime.strptime(m['time_'], '%Y-%m-%d %X').strftime('%m')
            if mon == month:
                month_query_list.append(m)
        json_data = json.dumps(month_query_list)
        print(json_data)
        return json_data

    def export_pdf(self, user):
        "导出文件至PDF"
        result_list = []
        result_list.append(f'{user.title()}的备忘录')
        with open(os.path.join(self.db_path, f'{user}.pkl'), 'rb') as f:
            datas = pickle.load(f)
        for m in datas:
            mm = memo.Memo(time_=m['time_'], thing=m['thing'], name=m['name'])
            result_list.append(str(mm))
        pdf = pdf_demo.ExportPDF(result_list, output_path=os.path.join(self.BASE_DIR, f'{user}.pdf'))
        pdf.save_text()
        self.logger.warning(f'导出{user.title()}的备忘录为PDF')

    def mail_send(self, user):
        "根据指定时间的内容通过邮件发送给用户"
        print('请选择需要发送整月还是整年的数据：  ')
        for k, v in self.mail_send_choose.items():
            print(f'{k}: {v}')
        choose = input('请输入前面的数字（‘q’退出）：')
        if choose == 'q':
            exit()
        elif choose != '1' and choose != '2':
            print('输入有误，请重新输入！')
            return self.mail_send()
        else:
            with open(os.path.join(self.db_path, f'{user}.pkl'), 'rb') as f:
                datas = pickle.load(f)
            choose_list = []
            if choose == '1':
                month = input('请输入月份：')
                for m in datas:
                    mon = datetime.strptime(m['time_'], '%Y-%m-%d %X').strftime('%m')
                    if mon == month:
                        choose_list.append(m)
                year = datetime.today().strftime('%Y')
                time_frame = f"{year}年{month}月"
            else:
                year = input('请输入年份：')
                for m in datas:
                    year_ = datetime.strptime(m['time_'], '%Y-%m-%d %X').strftime('%Y')
                    if year_ == year:
                        choose_list.append(m)
                time_frame = f'{year}年'

        # try:
        data = ''
        if choose_list == []:
            data = '您选择的时间段数据为空'
        else:
            for m in choose_list:
                mm = memo.Memo(time_=m['time_'], thing=m['thing'], name=m['name'])
                data = data + str(mm) + '\n'
        print(data)
        # toaddr = '214842382@qq.com'
        toaddr = self.config.read_config(user, 'email')
        mail = mailmaster.MailMaster(password='python123')
        mail.add_email_to_list(toaddr)
        mail.send_email_all(f'{time_frame}的备忘录数据', data)
        # except Exception as e:
        #     print(e)


def main():
    print('欢迎使用备忘录系统'.center(30, '*'))
    admin = MemoAdmin()
    user = admin.login()
    admin.choose_menu(user)


if __name__ == '__main__':
    main()
