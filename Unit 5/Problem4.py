def decrypt_story():
    code = CiphertextMessage(get_story_string())
    return code.decrypt_message()