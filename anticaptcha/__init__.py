import requests
import json, time

class AntiCaptcha():
	"""It`s SDK for API v.2 anti-captcha.com
	In this version u can work with Google NoCaptcha
	Example initialization SDK object:
	 anticaptcha = AntiCaptcha(api_key=YOUR_API_KEY, domain=API_REQUEST_DOMAIN)
	Default API_REQUEST_DOMAIN = https://api.anti-captcha.com/
	
	For create new task u must to use method createNoCaptchaTask, example:
		task = anticaptcha.createNoCaptchaTask(
			websiteURL="", 
			websiteKey="", 
			proxyType="", 
			proxyAddress="", 
			proxyPort="", 
			proxyLogin="", 
			proxyPassword="", 
			userAgent="",
			softId=0, # default 0
			languagePool="", # default "en"
			)
	In response u`ll get tuple. If first element of tuple is True, then in second element will be taskID as int, else in second element will be str with error description.
	taskID saved in anticaptcha.taskID

	For check result of task u must to use method getTaskResult, example:
		result = anticaptcha.getTaskResult(taskID=task[1])
	Default taskID = anticaptcha.taskID
	In response u`ll get tuple. If first element of tuple is True, then in second element will be SOLUTION element from API response, else in second element will be str with error description.

	U can to find more information about structure of request and response on official API documentation: https://anticaptcha.atlassian.net/wiki/display/API/API+v.2+Documentation
	GutHub page of this SDK: 
	Powered by AndreyPerelygin
	"""
	def __init__(self, api_key="", domain="https://api.anti-captcha.com/"):
		super(AntiCaptcha, self).__init__()
		self.api_key = api_key
		self.domain = domain
		self.req = requests.session()
		self.taskID = 0

	def _request(self, method="", data={}):
		url = self.domain + method
		headers = {'content-type': 'application/json'}

		response = self.req.post(url, data=json.dumps(data), headers=headers)
		if response.status_code == 200:
			return (True, json.loads(response.text))
		else:
			return (False, )

	def createNoCaptchaTask(
		self, 
		websiteURL="", 
		websiteKey="", 
		proxyType="", 
		proxyAddress="", 
		proxyPort="", 
		proxyLogin="", 
		proxyPassword="", 
		userAgent="",
		softId=0,
		languagePool="en"
		) -> tuple:

		request_data = {
		    "clientKey":self.api_key,
		    "task":
		        {
		            "type":"NoCaptchaTask",
		            "websiteURL":websiteURL,
		            "websiteKey":websiteKey,
		            "proxyType":proxyType,
		            "proxyAddress":proxyAddress,
		            "proxyPort":proxyPort,
		            "proxyLogin":proxyLogin,
		            "proxyPassword":proxyPassword,
		            "userAgent":userAgent
		        },
		    "softId":softId,
		    "languagePool":languagePool
		}

		response = self._request(method="createTask", data=request_data)
		if response[0] == True:
			if response[1]["errorId"] == 0:
				self.taskID = response[1]["taskId"]
				return (True, self.taskID)
			else:
				return (False, response[1]["errorCode"]+" "+response[1]["errorDescription"])
		else:
			return (False, "Bad HTTP Code")

	def getTaskResult(
		self, 
		taskID=0,
		) -> tuple:

		taskID = taskID if taskID != 0 else self.taskID

		request_data = {
		    "clientKey":self.api_key,
		    "taskId":taskID
		}

		response = self._request(method="getTaskResult", data=request_data)
		if response[0] == True:
			if response[1]["errorId"] == 0:
				if response[1]["status"] == "ready":
					return (True, response[1]["solution"]["gRecaptchaResponse"])
				else:
					print ("Task in processing")
					time.sleep(5)
					self.getTaskResult(taskID=taskID)
			else:
				return (False, response[1]["errorCode"]+" "+response[1]["errorDescription"])
		else:
			return (False, "Bad HTTP Code")