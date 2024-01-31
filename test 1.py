keys = {
    'биткоин': 'BTC',
    'эфириум': 'ETH',
    'доллар': 'USD'
}  #

# print(keys.keys())
# # print(keys.keys()[0])
#
# print(type(keys.keys()))
# print(type(list(keys.keys())))
# print(list(keys.keys())[0])
#
# for k in keys.keys():
#     print(k)
#
# print()

# import difflib as df
# import difflib


from difflib import SequenceMatcher


#
# b = 'эфириум'
# b = 'ЭФИРИУМ'
#
# df = 0
# for k in keys.keys():
#     var = SequenceMatcher(None, k, b).quick_ratio()
#     # if var > df:
#     #     df = var
#     if var > df: df = var

# def find_proper(req: str) -> str:
#     'Возвращает значение ва'
#     df = 0
#     proper= str()
#     for i, k in enumerate(keys.keys()):
#         var = SequenceMatcher(None, k, req).quick_ratio()
#         # if var > df:
#         #     df = var
#         if var > df:
#             df = var
#             proper = k
#         return proper
#
#
#
# req = 'эфириуM'
# find_proper(req)
# print(find_proper(req))


def find_proper(req: str) -> str:
    'Возвращает значение ва'
    df = 0
    proper = str()
    for i, k in enumerate(keys.keys()):

        var = SequenceMatcher(None, k, req).quick_ratio()
        # if var > df:
        #     df = var
        if var > df:
            df = var
            proper = k
    return proper


class Proper():
    @staticmethod
    def find(req: str) -> str:
        'Возвращает ключ из словаря keys, сходный с req'
        df = 0
        proper = str()
        for k in keys.keys():
            var = SequenceMatcher(None, k, req).quick_ratio()
            if var > df:
                df = var
                proper = k
        return proper



def find_proper(req: str) -> str:
    'Возвращает значение ва'
    df = 0
    proper = str()
    for i, k in enumerate(keys.keys()):

        var = SequenceMatcher(None, k, req).quick_ratio()
        # if var > df:
        #     df = var
        if var > df:
            df = var
            proper = k
    return proper
print('')
a = list(keys.keys())[0]
b = 'эфириум'
b = 'эфириуМ'

# s = SequenceMatcher(None, a, b)
# print(s.quick_ratio())

print(find_proper(b))
