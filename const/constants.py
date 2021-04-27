import re
from const.methods import Method

class Constant:

    @classmethod
    def all(cls):
        regex = r'^[A-Z][A-Z_]*[A-Z]$'
        return [kv for kv in cls.__dict__.items() if re.match(regex, kv[0])]


class METHOD(Constant):
    EXP = Method.Exponential
    RAYLE = Method.Rayle
    WEIBULL = Method.Weibull
    GAMMA = Method.Gamma
    NORMAL = Method.Normal

    _SWITCH_BY_ID_ = {
        0: EXP,
        1: RAYLE,
        2: WEIBULL,
        3: GAMMA,
        4: NORMAL
    }

    _SWITCH_BY_NAME_ = {
        "EXP": EXP,
        "RAYLE": RAYLE,
        "WEIBULL": WEIBULL,
        "GAMMA": GAMMA,
        "NORMAL": NORMAL
    }

    @classmethod
    def get_by_id(cls, idx):
        return METHOD._SWITCH_BY_ID_.get(idx)

    @classmethod
    def get_by_name(cls, name):
        return METHOD._SWITCH_BY_NAME_.get(name)


class TEXT(Constant):
    EXP = "Ցուցչային"
    RAYLE = "Ռեյլ"
    WEIBULL = "Վեյբուլ"
    GAMMA = "Գամմա"
    NORMAL = "Նորմալ"

    GENERAL_CASE = "Ընդհանուր դեպք"
    PRIMARY = "Հիմնական"
    MIXED = "Խառը"

    NOT_BACKUP = "Չպահուստավորված"
    BACKUP = "Պահուստավորված"
    PERMANENT = "Մշտական"
    REPLACEMENT = "Փոխարինումով"
    BY_ELEMENTS = "Ըստ տարերի"
    WHOLE = "Ընդհանուր"

    CB_NOT_RESTORED = "Չվերականգնվող համակարգ"
    CB_RESTORED = "Վերականգնվող համակարգ"

    TAB_CALC = "Հաշվարկ"
    TAB_DESC = "Մեթոդի նկարագրություն"

    LB_DESC = "Համառոտ նկարագրություն"
    LB_INPUT_DATA = "Մուտքային տվյալներ"
    LB_OUTPUT_DATA = "Ելքային տվյալներ"
    LB_MAIN_TITLE = "ԱՎՏՈՄԱՏԱՑՎԱԾ ՀԱՄԱԿԱՐԳԵՐԻ ՀՈՒՍԱԼԻՈՒԹՅԱՆ\n ՀԱՇՎԱՐԿԻ ՃԱՐՏԱՐԱԳԻՏԱԿԱՆ ՄԵԹՈԴՆԵՐ"
    LB_SYSTEM_TYPE = "Համակարգի տեսակը"
    LB_THE_SAME_VALUE = "Արժեքները նույնն են"
    LB_THE_BACKUP_ELM_COUNT = "Պահուստավորված տարերի քանակ (m)"
    LB_THE_SYSTEM_ELM_COUNT = "Համակարգի տարերի քանակ (n)"

    LB_ERR_CORRECT_DATA = "Մուտքագրել համապատասխան տվյալները"
    LB_ERR_WRONG_DATA = "Մուտքային տվյալները սխալ են"
    LB_ERR_ZERO_DIVISION = "Հաշվարկային սխալ (0֊ի բաժանում), \nխնդրում ենք ճշգրտել մուտքային տվյալները․"

    LEP_1_OR_MORE = "1 կամ ավելի"
    LEP_2_OR_MORE = "2 կամ ավելի"

    LB_LMD = "λ :"
    LB_MYU = "μ :"

    LB_t = "t :"
    LB_dt = "dt :"
    LB_N = "N :"

    TITLE_PROBABILITY = "Անխափան աշխատանքի  հավանականություն"
    TITLE_DISTRIBUTION = "Մինչև  համակարգի  խափանումը ընկած\n ժամանակահատվածի բաշխման խտություն"
    TITLE_FAILURE = "Համակարգի խափանման ուժգնություն"
    TITLE_READINESS = "Պատրաստակամության ֆունկցիա"
    TITLE_AT = "Անխափան աշխատանքի միջին ժամանակ"

    GR_T = "t"
    GR_AT = "T"
    GR_P = "$P_c(t)$"
    GR_F = "$f_c(t)$"
    GR_K = "$K_g(t)$"
    GR_LMD = "$\lambda_c(t)$"

    TABLE_T = "t"
    TABLE_P = "Pₕ(t)"
    TABLE_F = "fₕ(t)"
    TABLE_K = "Kₕ(t)"
    TABLE_LMD = "λₕ(t)"

    BTN_CREATE = "Ստեղծել"
    BTN_ADD = "Ավելացնել"
    BTN_CALCULATE = "Հաշվել"
    BTN_DELETE = "Ջնջել"
    BTN_CANCEL = "Չեղարկել"

    WINDOW_MAIN_TITLE = "RE-SYS [Ավտոմատացված համակարգերի հուսալիություն]"

    DIALOG_TITLE = "Ավելացնել համակարգ"

    MENU_FILE = "Ֆայլ"
    MENU_EDIT = "Խմբագրել"

    ABOUT_TITLE = "Մեր մասին"
    ABOUT_CONTENT = '''
        Ծրագիրը ստեղծվել է 2020 թվականին Վաչագան Գրիգորյանի կողմից ուսումնական նկատառումներով։
        Ստեղծված ծրագիրն հիմք է հանդիսանում ավարտական աշխատանքի համար։ Ծրագիրն անվճար է և թույլատրվում է օգտագործել միայն 
ուսումնական նպատակներով։
        Ծրագիրը ստեղծվել է Python 3 ծրագրավորման լեզվով։ Այստեղ օգտագործվել է մի շարք գրաֆիկական և մաթեմատիկական գրադարաներ, ինչպիսիք են PyQt5, MathPlot, Numpy, Scipy, Math և այլն։
        
        Հեղինակային բոլոր իրավունքները պաշտպանված են և պատկանում են Վաչագան Գրիգորյանին։
        
        Օգտվեք և հեշտացրեք ձեր աշխատանքը։
    '''


if __name__ == '__main__':
    print(Method.all())
