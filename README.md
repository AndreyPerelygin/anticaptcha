It`s SDK for API v.2 anti-captcha.com

In this version u can work with Google NoCaptcha

and image captcha.

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

For Image captcha use method createImageToTextTask, example:
```python
createImageToTextTask(
			self,
			body,
			phrase=False,
			case=False,
			math=False,
			maxLength=0,
			minLength=0,
			numeric=False,
			softId=0,
			languagePool="en"
			)
```
In response u`ll get tuple. If first element of tuple is True, then in second element will be taskID as int, else in second element will be str with error description.

taskID saved in anticaptcha.taskID

For check result of task u must to use method getTaskResult, example:
	
	result = anticaptcha.getTaskResult(taskID=task[1])

Default taskID = anticaptcha.taskID


For retrieve account balance u must to use method getBalance, example:

```python
result = anticaptcha.getBalance()
```

In response u`ll get tuple. If first element of tuple is True, then in second element will be SOLUTION element from API response, else in second element will be str with error description.

U can to find more information about structure of request and response on official API documentation: https://anticaptcha.atlassian.net/wiki/display/API/API+v.2+Documentation