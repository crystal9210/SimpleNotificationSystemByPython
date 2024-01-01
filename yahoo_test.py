import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

# attention!:this source does not function correctly.

# https://blog.css-net.co.jp/entry/2023/03/28/112402#%E5%89%8D%E6%8F%90%E6%9D%A1%E4%BB%B6
# 上のページは参考になるかも
def send_notification(subject, message, recepient_email, attachment_path=None):
  # YahooメールのSMTPサーバ設定
  smtp_server='smtp.mail.yahoo.co.jp'
  smtp_port=465

  # 送信元のYahooメアドとPW(パスワード)
  smtp_username='please paste your email address of yahoo.'
  # 環境変数からYahooメールのアプリパスワードを取得
  smtp_pw = os.environ.get('YAHOO_EMAIL_PASSWORD')
  # print(smtp_pw)

  if smtp_pw is None:
      print("環境変数 YAHOO_EMAIL_PASSWORD が設定されていません。")
      # エラー処理または終了処理を行う
  else:
      # SMTPサーバーへの認証など、パスワードを使用した処理を行う
    try:
      server=smtplib.SMTP(smtp_server, smtp_port)
      server.starttls()
      server.login(smtp_username,smtp_pw)

      # メールの構築
      msg=MIMEMultipart()
      msg['From']=smtp_username
      msg['To']=recepient_email
      msg['Subject']=subject

      # 本文を追加
      msg.attach(MIMEText(message, 'plain'))

      # 添付ファイルを追加
      if attachment_path:
        with open(attachment_path, "rb") as attachment_file:
          attachment=MIMEApplication(attachment_file.read(), _subtype="pdf")
        attachment.add_header('Content-Disposition', f'attachment; filename={attachment_path}')
        msg.attach(attachment)

      # メールの送信
      server.sendmail(smtp_username, recepient_email, msg.as_string())
      server.quit()
      print('通知が送信されました。')

    except Exception as e:
      print(f"通知の送信中にエラーが発生しました： {str(e)}")


if __name__ =="__main__":
  subject="テスト通知"
  message=input()
  recepient_email="please paste your email address of yahoo."

  send_notification(subject, message, recepient_email)






