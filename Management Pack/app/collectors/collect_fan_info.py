import requests

#def collect_fan_data(host_obj, fan):
#    # Push Thermall Fan API info
#    #host_obj.with_property("Hardware|Cooler|Fans|Name", fan["Name"])
#    fanName = fan["Name"]
#    host_obj.with_property(f"Hardware|Cooler|Fans|{fanName}|ID", fan["Id"])
#    host_obj.with_property(f"Hardware|Cooler|Fans|{fanName}|Health", fan["Status"]["Health"])
#    host_obj.with_property(f"Hardware|Cooler|Fans|{fanName}|State", fan["Status"]["State"])
#    host_obj.with_property(f"Hardware|Cooler|Fans|{fanName}|Hot Pluggable", fan["HotPluggable"])
#    host_obj.with_property(f"Hardware|Cooler|Fans|{fanName}|Speed RPM", fan["SpeedPercent"]["SpeedRPM"])
#    host_obj.with_property(f"Hardware|Cooler|Fans|{fanName}|Service Label", fan["Location"]["PartLocation"]["ServiceLabel"])
#    host_obj.with_property(f"Hardware|Cooler|Fans|{fanName}|Fan Type", fan["Oem"]["Dell"]["FanType"])
#    host_obj.with_property(f"Hardware|Cooler|Fans|{fanName}|Fan PWM", fan["Oem"]["Dell"]["FanPWM"])


#def collect_fan_data(host_obj, fan):
#    # Helper function to handle None values
#    def safe_get(value, default="null"):
#        return value if value is not None else default
#
#    # Push Thermal Fan API info
#    fanName = safe_get(fan.get("Name"))
#    host_obj.with_property(f"Hardware|Cooler|Fans|{fanName}|ID", safe_get(fan.get("Id")))
#    host_obj.with_property(f"Hardware|Cooler|Fans|{fanName}|Health", safe_get(fan.get("Status", {}).get("Health")))
#    host_obj.with_property(f"Hardware|Cooler|Fans|{fanName}|State", safe_get(fan.get("Status", {}).get("State")))
#    host_obj.with_property(f"Hardware|Cooler|Fans|{fanName}|Hot Pluggable", safe_get(fan.get("HotPluggable")))
#    host_obj.with_property(f"Hardware|Cooler|Fans|{fanName}|Speed RPM", safe_get(fan.get("SpeedPercent", {}).get("SpeedRPM")))
#    host_obj.with_property(f"Hardware|Cooler|Fans|{fanName}|Service Label", safe_get(fan.get("Location", {}).get("PartLocation", {}).get("ServiceLabel")))
#    host_obj.with_property(f"Hardware|Cooler|Fans|{fanName}|Fan Type", safe_get(fan.get("Oem", {}).get("Dell", {}).get("FanType")))
#    host_obj.with_property(f"Hardware|Cooler|Fans|{fanName}|Fan PWM", safe_get(fan.get("Oem", {}).get("Dell", {}).get("FanPWM")))

def check_value(data, keys, default="null"):
    try:
        for key in keys:
            data = data.get(key) if isinstance(data, dict) else None
        return data if data is not None else default
    except Exception:
        return default

def collect_fan_data(host_obj, fan):
    fanName = check_value(fan, ["Name"])
    host_obj.with_property(f"Hardware|Cooler|Fans|{fanName}|ID", check_value(fan, ["Id"]))
    host_obj.with_property(f"Hardware|Cooler|Fans|{fanName}|Health", check_value(fan, ["Status", "Health"]))
    host_obj.with_property(f"Hardware|Cooler|Fans|{fanName}|State", check_value(fan, ["Status", "State"]))
    host_obj.with_property(f"Hardware|Cooler|Fans|{fanName}|Hot Pluggable", check_value(fan, ["HotPluggable"]))
    host_obj.with_property(f"Hardware|Cooler|Fans|{fanName}|Speed RPM", check_value(fan, ["SpeedPercent", "SpeedRPM"]))
    host_obj.with_property(f"Hardware|Cooler|Fans|{fanName}|Service Label", check_value(fan, ["Location", "PartLocation", "ServiceLabel"]))
    host_obj.with_property(f"Hardware|Cooler|Fans|{fanName}|Fan Type", check_value(fan, ["Oem", "Dell", "FanType"]))
    host_obj.with_property(f"Hardware|Cooler|Fans|{fanName}|Fan PWM", check_value(fan, ["Oem", "Dell", "FanPWM"]))