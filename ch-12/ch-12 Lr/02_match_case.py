def http_status(status):
      match status:
            case 200:
                  return "ok"
            case 304:
                  return "not found"
            case 400:
                  return "interal server Error "
            
            case _:
                  return "unknown status"
            
print(http_status(304))
            


