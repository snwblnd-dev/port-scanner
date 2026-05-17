from api.routers import scans

from fastapi import FastAPI


app = FastAPI()
app.include_router(scans.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
#def main():
    #the original cmd line scanner test
    # parser = create_parser()
    # args = parser.parse_args()
    # scanner = PortScanner(hostname=args.url, max_port=args.port, semaphore=args.semaphore)







    # scanner = PortScanner(hostname='scanme.nmap.org', max_port=1024, semaphore=500)
    # try:
    #     asyncio.run(scanner.scan_ports())
    # except KeyboardInterrupt as e:
    #     print(e)



# if __name__ == '__main__':
#     main()


