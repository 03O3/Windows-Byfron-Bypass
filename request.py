from mitmproxy import http
    
def request(flow: http.HTTPFlow) -> None:
    if "https://www.roblox.com/mobileapi/check-app-version?appVersion=AppUWPV2.592.586" in flow.request.pretty_url:
        
        response_content = b'{"data":{"UpgradeAction":"None"}}'
        flow.response = http.Response.make(
            200,  
            response_content,
            {"Content-Type": "application/json"}
        )

addons = [
    request
]
