import requests

def webHook(message,webHookUrl):
	data = {"content": message}
	response = requests.post(webHookUrl, json=data)
	return response.status_code

if __name__ == "__main__":

	webHookUrl = "https://discord.com/api/webhooks/818963xxxxxxxxxx338354/BJN07SsarO-Ixxxxxxxxxxxxxxxxu47D4kheCJXxOhPsP0Ije0M9QorlETpGTqT4i_"
	message = "Hello World!"

	webHook(message,webHookUrl)
