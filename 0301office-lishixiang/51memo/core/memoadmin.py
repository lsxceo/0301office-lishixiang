#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# memoadmin.py
# author: lishixiang

import os
import logging
import pickle
import time
from . import  create_event, configadmin, log_ctrl, memo, setting, pdf_demo


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
                # self.logger.info("添加新用户的配置信息")  # 添加日志文件

                # 添加到日志文件
                self.logger.warning("新用户%s已创建" %user)
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
                with open(os.path.join(self.db_path, f'{user}.pkl'), 'rb') as f:
                    datas = pickle.load(f)
                func = getattr(self, self.menu[choose], datas)
                func(user, datas=datas)
        except Exception as e:
            print(f"输入有误：错误为'{e}''")
        time.sleep(2)
        return self.choose_menu(user)


    def add(self, user, datas):
        "增加备忘录条目"
        event = input('请输入要添加的备忘事项：(示例：明天下午2点开会@小李@小王)')
        create = create_event.Create_event(event)
        split_list = create.split_list
        newmemo = memo.Memo(split_list[0], split_list[1], split_list[2], split_list[3], split_list[4], split_list[5])
        memo_dict = newmemo.memo_dict()
        num_list = []
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

    def delete(self, user, datas):
        "删除备忘录条目"
        for m in datas:
            mm = memo.Memo(m['date'], m['frame'], m['hour'], m['minute'], m['thing'], m['name'])
            print(f'ID: {m["id"]}   {mm}')
        id = input('请输入要删除的备忘事项的ID： ')
        for m in datas:
            if m['id'] == int(id):
                del_id = int(id)
                del_memo = memo.Memo(m['date'], m['frame'], m['hour'], m['minute'], m['thing'], m['name'])
                datas.remove(m)
                self.logger.warning(f'删除条目-ID: {del_id} {del_memo}')  # 打印出删除备忘录的信息
        with open(os.path.join(self.db_path, user + '.pkl'), 'wb') as f:
            pickle.dump(datas, f)

    def modify(self, user, datas):
        "修改备忘录条目"
        last_memo = {}
        for m in datas:
            mm = memo.Memo(m['date'], m['frame'], m['hour'], m['minute'], m['thing'], m['name'])
            print(f'ID: {m["id"]}   {mm}')
        num = int(input('请输入你要修改的备忘事项的ID： '))
        event = input('请输入修改后的事项： ')
        create = create_event.Create_event(event)
        split_list = create.split_list
        memonew = memo.Memo(split_list[0], split_list[1], split_list[2], split_list[3], split_list[4], split_list[5])
        memo_dict = memonew.memo_dict()
        for m in datas:
            if m['id'] == num:
                # 找出修改前的字典
                last_memo['date'] = m['date']
                last_memo['frame'] = m['frame']
                last_memo['hour'] = m['hour']
                last_memo['minute'] = m['minute']
                last_memo['thing'] = m['thing']
                last_memo['name'] = m['name']
                # 修改字典
                m['date'] = memo_dict['date']
                m['frame'] = memo_dict['frame']
                m['hour'] = memo_dict['hour']
                m['minute'] = memo_dict['minute']
                m['thing'] = memo_dict['thing']
                m['name'] = memo_dict['name']

                before_memo = memo.Memo(last_memo['date'], last_memo['frame'], last_memo['hour'], last_memo['minute'], last_memo['thing'], last_memo['name'])
                # current_memo = memo.Memo(memo_dict['date'], memo_dict['frame'], memo_dict['hour'], memo_dict['minute'], memo_dict['thing'], memo_dict['name'])
                self.logger.warning(f'备忘录修改成功！ID: {num}  {before_memo} 修改为 {memonew}')  # 打印出修改备忘录的信息
        with open(os.path.join(self.db_path, user + '.pkl'), 'wb') as f:
            pickle.dump(datas, f)

    def query(self, user, datas):
        "查询备忘录条目"
        for m in datas:
            mm = memo.Memo(m['date'], m['frame'], m['hour'], m['minute'], m['thing'], m['name'])
            print(mm)
        print('- -'*15)
        self.logger.info('查看备忘录列表')


    def export_pdf(self, user, datas):
        "导出文件至PDF"
        result_list = []
        result_list.append(f'{user.title()}的备忘录')
        for m in datas:
            mm = memo.Memo(m['date'], m['frame'], m['hour'], m['minute'], m['thing'], m['name'])
            result_list.append(str(mm))
        pdf = pdf_demo.ExportPDF(result_list, output_path=os.path.join(self.BASE_DIR, f'{user}.pdf'))
        pdf.save_text()
        self.logger.warning(f'导出{user.title()}的备忘录为PDF')

    
def main():
    print('欢迎使用备忘录系统'.center(30, '*'))
    admin = MemoAdmin()
    user = admin.login()
    admin.choose_menu(user)
    



if __name__ == '__main__':
    main()
    