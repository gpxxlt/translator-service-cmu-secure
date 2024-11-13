from src.translator import translate_content


def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert translated_content == "This is a Chinese message"

def test_hindi():
    is_english, translated_content = translate_content("यह हिंदी में संदेश है")
    assert is_english == False
    assert translated_content == "This is a Hindi message"

def test_english():
    is_english, translated_content = translate_content("This is an English message")
    assert is_english == True
    assert translated_content == "This is an English message"

def test_turkish():
    is_english, translated_content = translate_content("Bu bir Türkçe mesajdır")
    assert is_english == False
    assert translated_content == "This is a Turkish message"

def test_russian():
    is_english, translated_content = translate_content("Это сообщение на русском")
    assert is_english == False
    assert translated_content == "This is a Russian message"

def test_llm_normal_response():
    pass

def test_llm_gibberish_response1():
    is_english, translated_content = translate_content("🥲")
    assert is_english == False
    assert translated_content != "This is a English message"

def test_llm_gibberish_response2():
    is_english, translated_content = translate_content("30498230f")
    assert is_english == False
    assert translated_content != "This is a English message"

def test_llm_gibberish_response3():
    is_english, translated_content = translate_content("......")
    assert is_english == False
    assert translated_content != "This is a English message"