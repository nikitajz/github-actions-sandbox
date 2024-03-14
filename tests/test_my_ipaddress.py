from src.pkg.my_ipaddress import get_my_ip_address


def test_get_my_ip_address():
    # check if the function returns a string, which is the IP address format
    assert isinstance(get_my_ip_address(), str)
    assert get_my_ip_address().count(".") == 3
