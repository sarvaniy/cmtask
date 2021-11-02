# cmtask repo
This repo provides two apis to fetch the exchange rate for BTC/USD and also force requesting the prices from alphavantage.
Also supports periodic task for every 1 hour it will trigger and fetch the BTC/USD exchange rate from alphavantage API

### setup and test

install docker-compose and docker

clone the code

Get into the repo code and bringup the containers via docker-compose.yml with below command

ex: docker-compose build
    docker-compose up

Test the Apis and See the example for reference

  ex: curl http://localhost:8002/api/v1/quotes -X POST
    
     {"status":"success","data":{"2021-11-02":{"1a. open (USD)":"60911.12000000","1b. open (USD)":"60911.12000000","2a. high (USD)":"61399.00000000","2b. high (USD)":"61399.00000000","3a. low (USD)":"60634.99000000","3b. low (USD)":"60634.99000000","4a. close (USD)":"60725.68000000","4b. close (USD)":"60725.68000000","5. volume":"1386.58244000","6. market cap (USD)":"1386.58244000"}}}


     curl http://localhost:8002/api/v1/quotes -X GET

     {"status":"success","data":{"id":1,"from_currency":"BTC","to_currency":"USD","ex_rate":"61749.77000000"}}

     curl http://localhost:8002/api/v1/quotes -X PUT

     {"detail":"Method \"PUT\" not allowed."}



