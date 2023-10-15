from fuel import convert, gauge

def test_percent():
    assert gauge(convert("3/4")) == "75%"  
    assert gauge(convert("1/4")) == "25%"  

def test_Full():
    assert gauge(convert("4/4")) == "F"  

def test_E():
    assert gauge(convert("0/4")) == "E"  
