from unittest.mock import Mock
import with_reduce

def test_get_total_bytes():
    src = "192.168.13.10"
    data = [{"src_ip":"192.168.13.10", "total_bytes":3},{"src_ip":"192.168.13.10", "total_bytes":7},{"src_ip":"192.168.12.10", "total_bytes":7}]
    result = with_reduce.get_total_bytes(src, data)
    assert result == 10

def test_load_data():
    data = Mock()
    data.load_data.return_value = [{"src_ip":"192.168.13.10", "total_bytes":3},{"src_ip":"192.168.13.10", "total_bytes":7}]
    assert data.load_data() == [{"src_ip":"192.168.13.10", "total_bytes":3},{"src_ip":"192.168.13.10", "total_bytes":7}]

def test_get_src_ip():
    data = [{"src_ip":"192.168.13.10", "total_bytes":3},{"src_ip":"192.168.13.10", "total_bytes":7}]
    result = with_reduce.get_src_ip(data)
    assert result == ["192.168.13.10"]

def test_calc_total_bytes():
    data = [{"src_ip":"192.168.13.10", "total_bytes":3},{"src_ip":"192.168.13.10", "total_bytes":7},{"src_ip":"192.168.12.10", "total_bytes":7}]
    src_ip = ["192.168.13.10","192.168.12.10"]
    result = with_reduce.calc_total_bytes(src_ip, data)
    assert result == {"192.168.13.10": 10,"192.168.12.10": 7}
