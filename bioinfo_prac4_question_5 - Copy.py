# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:46:54 2018

@author: kumar
"""


def common_pentapeptide_between_org(x,y):
    penta_x = []
    penta_y = []
    for i in range(len(y)-4):
        penta_x.append(x[i:i+5])
        penta_y.append(y[i:i+5])
    common = list(set(penta_y).intersection(penta_x))
    print(common)
    print("Occurrences_common pentapeptides in chicken_hemoglobin")
    for i in range(len(common)):
        print(common[i],penta_y.count(common[i]))
    
    print("Occurrences_common pentapeptides in human_hemoglobin")
    for i in range(len(common)):
        print(common[i],penta_x.count(common[i]))
human='MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH'
chicken='MVHWTAEEKQLITGLWGKVNVAECGAEALARLLIVYPWTQRFFASFGNLSSPTAILGNPMVRAHGKKVLTSFGDAVKNLDNIKNTFSQLSELHCDKLHVDPENFRLLGDILIIVLAAHFSKDFTPECQAAWQKLVRVVAHALARKYH'

print(common_pentapeptide_between_org(human,chicken))