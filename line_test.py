import requests

def send_line_notification(token, message):
  url="https://notify-api.line.me/api/notify"
  headers={'Authorization':f'Bearer {token}'}
  data={'message':message}

  response=requests.post(url, headers=headers, data=data)

  if response.status_code==200:
    print("LINE通知が送信されました")
  else:
    print(f"LINE通知の送信中にエラーが発生しました:{response.text}")

if __name__=="__main__":
  line_notify_token="Please paste the token generated from the LINE Notify developer page here."

  message=input()

  send_line_notification(line_notify_token,message)
