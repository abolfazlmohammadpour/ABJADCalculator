ABJADListArabic = dict()
ABJADListPersian = dict()

UnSupportedCharacters = list()
UnSupportedAlphabetics = list()

ABJADListArabic["ذ"] = int(700)
ABJADListArabic["ض"] = int(800)
ABJADListArabic["ص"] = int(90)
ABJADListArabic["ث"] = int(500)
ABJADListArabic["ق"] = int(100)
ABJADListArabic["ف"] = int(80)
ABJADListArabic["غ"] = int(1000)
ABJADListArabic["ع"] = int(70)
ABJADListArabic["ه"] = int(5)
ABJADListArabic["خ"] = int(600)
ABJADListArabic["ح"] = int(8)
ABJADListArabic["ج"] = int(3)
ABJADListArabic["د"] = int(4)
ABJADListArabic["ش"] = int(300)
ABJADListArabic["س"] = int(60)
ABJADListArabic["ي"] = int(10)
ABJADListArabic["ب"] = int(2)
ABJADListArabic["ل"] = int(30)
ABJADListArabic["ا"] = int(1)
ABJADListArabic["أ"] = int(1)
ABJADListArabic["إ"] = int(1)
ABJADListArabic["ت"] = int(400)
ABJADListArabic["ن"] = int(50)
ABJADListArabic["م"] = int(40)
ABJADListArabic["ك"] = int(20)
ABJADListArabic["ط"] = int(9)
ABJADListArabic["ئ"] = int(10)
ABJADListArabic["ء"] = int(1)
ABJADListArabic["ؤ"] = int(6)
ABJADListArabic["ر"] = int(200)
ABJADListArabic["ى"] = int(10)
ABJADListArabic["ة"] = int(5)
ABJADListArabic["و"] = int(6)
ABJADListArabic["ز"] = int(7)
ABJADListArabic["ظ"] = int(900)

ABJADListPersian = ABJADListArabic.copy()
ABJADListPersian["پ"] = int(2)
ABJADListPersian["چ"] = int(3)
ABJADListPersian["ژ"] = int(7)
ABJADListPersian["گ"] = int(20)
ABJADListPersian["ک"] = int(20)
ABJADListPersian["ا"] = int(1)
ABJADListPersian["آ"] = int(20)
ABJADListPersian["ی"] = int(10)

UnSupportedCharacters = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\'', '\"', ';', ':', '/', '?', '.', ',', '<', '>', '\\', ' ']
UnSupportedAlphabetics = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
UnSupportedAlphabetics += ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']