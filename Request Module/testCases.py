import script
import pytest

@pytest.mark.staus_code
def test_w3_status_code():
        result=script.w3schools_API.w3_status_code()
        assert result == 200

@pytest.mark.header
def test_w3_header():
        result=script.w3schools_API.w3_headers()
        assert result == {'Content-Encoding': 'gzip', 
                          'Accept-Ranges': 'bytes', 
                          'Age': '10152', 
                          'Cache-Control': 'public,max-age=14400,public' , 
                          'Content-Security-Policy': "frame-ancestors 'self' https://mycourses.w3schools.com;", 
                          'Content-Type': 'text/html' , 
                          'Date': 'Thu, 11 Jan 2024 12:45:57 GMT' , 
                          'Etag': '"0c3a8336344da1:0+gzip"', 
                          'Last-Modified': 'Thu, 11 Jan 2024 07:53:02 GMT' , 
                          'Server': 'ECS (nag/9998)' , 
                          'Vary': 'Accept-Encoding' , 
                          'X-Cache': 'HIT' , 
                          'X-Content-Security-Policy': "frame-ancestors 'self' https://mycourses.w3schools.com;" , 
                          'X-Powered-By': 'ASP.NET' , 
                          'Content-Length': '78'}
        
def test_negative_w3_code():
        result=script.w3schools_API.w3_error_code()
        assert result == 404

@pytest.mark.text
def test_w3_text():
        result=script.w3schools_API.w3_text()
        assert result == """<!DOCTYPE html>
<html>
<body>

<h1>This is a Test Page</h1>

</body>
</html>"""


@pytest.mark.text
def test_dummy_text():
        result=script.dummy_API.dummy_text()
        assert result == '{\"status\":"success","data":[{"id":1,"employee_name":"Tiger Nixon","employee_salary":320800,"employee_age":61,"profile_image":""},{"id":2,"employee_name":"Garrett Winters","employee_salary":170750,"employee_age":63,"profile_image":""},{"id":3,"employee_name":"Ashton Cox","employee_salary":86000,"employee_age":66,"profile_image":""},{"id":4,"employee_name":"Cedric Kelly","employee_salary":433060,"employee_age":22,"profile_image":""},{"id":5,"employee_name":"Airi Satou","employee_salary":162700,"employee_age":33,"profile_image":""},{"id":6,"employee_name":"Brielle Williamson","employee_salary":372000,"employee_age":61,"profile_image":""},{"id":7,"employee_name":"Herrod Chandler","employee_salary":137500,"employee_age":59,"profile_image":""},{"id":8,"employee_name":"Rhona Davidson","employee_salary":327900,"employee_age":55,"profile_image":""},{"id":9,"employee_name":"Colleen Hurst","employee_salary":205500,"employee_age":39,"profile_image":""},{"id":10,"employee_name":"Sonya Frost","employee_salary":103600,"employee_age":23,"profile_image":""},{"id":11,"employee_name":"Jena Gaines","employee_salary":90560,"employee_age":30,"profile_image":""},{"id":12,"employee_name":"Quinn Flynn","employee_salary":342000,"employee_age":22,"profile_image":""},{"id":13,"employee_name":"Charde Marshall","employee_salary":470600,"employee_age":36,"profile_image":""},{"id":14,"employee_name":"Haley Kennedy","employee_salary":313500,"employee_age":43,"profile_image":""},{"id":15,"employee_name":"Tatyana Fitzpatrick","employee_salary":385750,"employee_age":19,"profile_image":""},{"id":16,"employee_name":"Michael Silva","employee_salary":198500,"employee_age":66,"profile_image":""},{"id":17,"employee_name":"Paul Byrd","employee_salary":725000,"employee_age":64,"profile_image":""},{"id":18,"employee_name":"Gloria Little","employee_salary":237500,"employee_age":59,"profile_image":""},{"id":19,"employee_name":"Bradley Greer","employee_salary":132000,"employee_age":41,"profile_image":""},{"id":20,"employee_name":"Dai Rios","employee_salary":217500,"employee_age":35,"profile_image":""},{"id":21,"employee_name":"Jenette Caldwell","employee_salary":345000,"employee_age":30,"profile_image":""},{"id":22,"employee_name":"Yuri Berry","employee_salary":675000,"employee_age":40,"profile_image":""},{"id":23,"employee_name":"Caesar Vance","employee_salary":106450,"employee_age":21,"profile_image":""},{"id":24,"employee_name":"Doris Wilder","employee_salary":85600,"employee_age":23,"profile_image":""}],"message":"Successfully! All records has been fetched."}'

@pytest.mark.staus_code
def test_status_code():
        result=script.dummy_API.dummy_status_code()
        assert result == 200

    
@pytest.mark.header
def test_header():
        result=script.dummy_API.dummy_headers()
        assert result=={'Cache-Control': 'public, max-age=2592000', 'Content-Encoding': 'gzip', 'Content-Type': 'application/json', 'Date': 'Thu, 11 Jan 2024 12:53:55 UTC', 'Display': 'staticcontent_sol, orig_site_sol', 'Response': '200', 'Server': 'nginx/1.21.6', 'Vary': 'Accept-Encoding,User-Agent,Origin', 'X-Endurance-Cache-Level': '2', 'X-Ezoic-Cdn': 'Hit ds;mm;50851011b4bdbba5d4a9e6d8cab4c54f;2-133674-15;b1402895-60a9-43a7-77c2-829f1bc2194d', 'X-Middleton-Display': 'staticcontent_sol, orig_site_sol', 'X-Middleton-Response': '200', 'X-Nginx-Cache': 'WordPress', 'X-Origin-Cache-Control': 'no-cache, private', 'X-Ratelimit-Limit': '60', 'X-Ratelimit-Remaining': '58', 'X-Server-Cache': 'false', 'X-Sol': 'orig', 'Transfer-Encoding': 'chunked'}