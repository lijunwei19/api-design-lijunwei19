import requests

from pprintpp import pprint as pp

def weather_data_download(id, country):

  if type(id) == str :

    parameter = "q=" + id

  elif type (id) == tuple :

    i, j = id

    country=""

    parameter = "lat={}&lon={}".format(int(i),int(j))

  elif type(id) == int :
    
    if len(str(id)) == 7 :

      parameter = "id=" + str(id)

    elif len(str(id)) == 5:

      parameter = "zip=" + str(id)
    
    else:
    
      raise TypeError ("Please input valid int city name or zip or id")
  else:
    
    raise TypeError ("Please input valid city name or zip or id")

  url = 'https://openweathermap.org/data/2.5/weather?{},{}&appid=b6907d289e10d714a6e88b30761fae22'.format(parameter, country)

  # print(url)
 
  Json_data = requests.get(url).json()
  
  pp (Json_data)
  
  if "message" in Json_data:
  
    return False
  
  else:
  
    return True 


# def main():

#   print(weather_data_download(65201, "us"))


# if __name__ == '__main__':

#   main()
#   