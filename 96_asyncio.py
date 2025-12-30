import asyncio
import requests

async def fn1():
    '''
    HERE CAN'T USE THE TIME.SLEEP AS IT PUTS WHOLE CODE TO STOP
    INSTEAD USING AWAIT ASYNC SLEEP ONLY PUTS THAT INDIVIDUAL FN TO SLEEP
    '''
    # await asyncio.sleep(2)
    print('fn 1')
    url = "https://svs.gsfc.nasa.gov/14933#media_group_379229"
    response = requests.get(url)
    open("nasaImage1.jpg","wb").write(response.content)
    
async def fn2():
    # await asyncio.sleep(2)
    print('fn 2')
    url = "https://www.nasa.gov/wp-content/uploads/2025/11/potm2510a.jpg"
    response = requests.get(url)
    open("nasaImage2.jpg","wb").write(response.content)
    return "u"
async def fn3():
    # await asyncio.sleep(5)
    print('fn 3')
    url = "https://www.nasa.gov/wp-content/uploads/2025/11/hubble-ngc2775-potw2538a.jpg"
    response = requests.get(url)
    open("nasaImage3.jpg","wb").write(response.content)

async def main():
    
    M = await asyncio.gather(
        fn1(),
        fn2(),
        fn3()  ) 
    return 2
        #teeno parallely chal rhe hai   bass image ki size jayada and kam ho rhi hai
    print(M)
    task = asyncio.create_task(fn1()) #'''not good for organisation'''
    await fn1()
    await fn2()
    await fn3()
    
asyncio.run(main())