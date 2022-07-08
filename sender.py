#Sends to phone number of choice
def runner():
    from sympy import im
    from index import initlib as api
    Num = '1232231234'
    response = api.api_send(Num)
    return (str(response))

if __name__ == '__main__':
    runner()