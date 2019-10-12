#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# mailmaster.py


import smtplib
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


class MailMaster:
    """邮箱大师"""
    def __init__(self, password, smtp_sever='smtp.yeah.net', debuglevel=0, email_from='lsxceo@yeah.net'):
        self.smtp = SMTP_SSL(smtp_sever)
        self.smtp.set_debuglevel(debuglevel)
        self.smtp.ehlo(smtp_sever)
        self.smtp.login(email_from, password)
        self.email_from = email_from
        self.email_to = []

    def add_email_to_list(self, email_addr):
        return self.email_to.append(email_addr)

    def notice(self, username, text, subject='通知信息'):
        self.send_email_all(subject, f'{username}\n' + text)

    def send_email_all(self, subject, body, mailtype='plain', attachment=None):
        """
        发送邮件通用接口
        subject: 邮件标题
        body: 邮件内容
        mailtype: 邮件类型，默认是文本，发html时候指定为html
        attachment: 附件
        """
        msg = MIMEMultipart()  # 构造一个MIMEMultipart对象代表邮件本身
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = self.email_from
        try:
            if len(self.email_to) > 0:
                to_email = self.email_to
                msg['To'] = ','.join(to_email)
            else:
                raise smtplib.SMTPRecipientsRefused('没有收件人，请用add_email_list_to添加')

            # mailtype代表邮件类型，纯文本或html等
            msg.attach(MIMEText(body, mailtype, 'utf-8'))

            # 有附件内容，才添加到邮件
            if attachment:
                # 二进制方式模式文件
                with open(attachment, 'rb') as f:
                    # MIMEBase表示附件的对象
                    mime = MIMEBase('text', 'txt', filename=attachment)
                    # filename是显示附件名字
                    mime.add_header('Content-Disposition', 'attachment', filename=attachment)
                    # 获取附件内容
                    mime.set_payload(f.read())
                    encoders.encode_base64(mime)
                    # 作为附件添加到邮件
                    msg.attach(mime)
            self.smtp.sendmail(self.email_from, self.email_to, msg.as_string())
            self.smtp.quit()
        except smtplib.SMTPException as e:
            print(e)


def main():
    toaddr = '214842382@qq.com'
    html = """
    <h1>第8哥的邮件啊</h1>
    <h2>须有html格式, 比如写个表格</h2>
    <table border="1">
        <tr>
            <th>姓名</th>
            <th>城市</th>
        </tr>
        <tr>
            <td>第8哥</td>
            <td>北京</td>
        </tr>
    </table>
    """
    mail = MailMaster(password='python123')
    mail.add_email_to_list(toaddr)
    # mail.notice('Bruce, Hi, This is an email sent by python!')
    mail.send_email_all('Python测试', html, mailtype='html')


if __name__ == '__main__':
    main()
