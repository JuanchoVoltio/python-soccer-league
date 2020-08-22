import datetime


def get_formatted_laptime(seconds=0, milliseconds=0):

    timedelta = time_delta = datetime.timedelta(seconds = seconds)
    
    if milliseconds > 0:
        converted_microsecs = ((seconds*1000) + milliseconds) * 1000
        time_delta = datetime.timedelta(microseconds = converted_microsecs)

    return '%s' % (str(time_delta))
  
get_formatted_laptime.__doc__ = "Recibe los segundos o millisegundos a convertir en formato hh:mm:ss.fff"
