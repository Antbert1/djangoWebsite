from django import template

register = template.Library()

@register.simple_tag
def getDateMonth(dateSent):
    month = dateSent.strftime("%m")
    # yearDict = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    yearDict = {
        "01": "Jan",
        "02": "Feb",
        "03": "Mar",
        "04": "Apr",
        "05": "May",
        "06": "Jun",
        "07": "Jul",
        "08": "Aug",
        "09": "Sept",
        "10": "Oct",
        "11": "Nov",
        "12": "Dec"
    }
    return yearDict[month]
