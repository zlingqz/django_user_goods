#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
print(sys.path)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, 'user'))
sys.path.append(os.path.join(BASE_DIR, 'goods'))


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_15.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    from user.models import User
    from goods.models import Category
    # from . import user,goods
    import random
    import datetime
    from hashlib import md5

    def build_user():
        name_s = ['张伟', '王伟', '王芳', '李伟', '王秀英', '李秀英', '李娜', '张秀英', '刘伟',
                  '张敏', '李静', '张丽', '王静', '王丽', '李强', '张静', '李敏', '王敏', '王磊',
                  '李军', '刘洋', '王勇', '张勇', '王艳', '李杰 ', '张磊 ', '王强 ', '王军 ', '张杰 ', '李娟 ', '张艳 ', '张涛 ', '王涛 ', '李明 ', '李艳 ', '王超 ', '李勇 ', '王娟 ', '刘杰 ', '王秀兰 ', '李霞 ', '刘敏 ', '张军 ', '李丽 ', '张强 ', '王平 ', '王刚 ', '王杰 ', '李桂英 ', '刘芳', ]
        for i in range(len(name_s)):
            # user.models.User(
            User(
                account = '%05d' % i,
                name = name_s[i],
                # img = 'img/%s.png' % i,os.path.join('img', '%s.png')
                img = os.path.join('img', '%s.png') % i,
                password = md5(str(i).encode('ascii')).hexdigest(),
                gender = random.choice([0, 1]),
                tel = str(random.choice([1346,1350,1351,1360,1370,1372,1380,1390,1391,1590,1881,])) + str(random.randint(1000000, 9999999)),
                email = '%05d@qq.com' % i,
                state = random.choice([1]*10+[2]*2+[3]*1),
                createDatetime = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 60))
            ).save()

    def build_category():
        h1_s = ['手机', '运动鞋']
        h2_s = [['华为','苹果','小米','oppo','vivo','三星','魅族','联想','飞利浦','索尼','酷派'],
                ['耐克','安踏','特步','361','乔丹','贵人年','adidas']]
        pcategory = []
        for i in range(len(h1_s)):
            pcategory.append(Category.objects.create(name=h1_s[i],path='/category/%s' % (i + 1)))

        for i in range(len(h2_s)):
            for j in range(len(h2_s[i])):
                Category.objects.create(name=h2_s[i][j], path='/category/%s-%s' % (i + 1, j + 1),
                                        pcategory=pcategory[i])

    build_user()
    build_category()


if __name__ == '__main__':
    main()
