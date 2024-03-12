from fastapi.responses import JSONResponse

def make_response(payload: dict = {}, message: str = 'success', meta: dict = {}, code: int = 200):
    if code == 200:
        return JSONResponse(content={"code": code, "meta":meta, "success":True, "message": message, "data": payload})
    else:
        return JSONResponse(content={"code": code, "meta":meta, "success":False, "message": message, "data": payload})