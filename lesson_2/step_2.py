"""
GIT


https://git-scm.com/book/ru/v1/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B-Git
-- Централизованные
SVN
-repo 1

-- Распределенная система
GIT
-repo n n = count of developers




проверка гита на наличие
команда git в консоли



АРГУМЕНТЫ
-- полное имя
или -

конструкция команды
cmd --argument=   ==help -h


папку .git не удалять - папка локального репозитория


присоединение к проекту (получить существующий) - делать гитклон из общего репозитория, преобразовывать в локальный
git init
git clone url

git add - добавление файлов в индекс

git commit и обязательно конструкцию -m


git log
первые 7 символов - хэш коммита, по нему его можно искать


git checkout
отмена локальных изменений до индексации


git reset HEAD <файл> - сброс последних изменений перед коммитом (убрать из индекса)


ВЕТКИ
git branch - показать все ветки
git checkout - создать ветку

git checkout -b dev_master


git checkout <hash> - перемещение по истории коммитов


ДАНЖЕР!!!
если внесли изменения без индексации и коммита в одной ветке и перешли в другую ветку, то эти изменения перенесутся в новую ветку.
поэтому надо фиксировать изменения
бояться буквы М в репорте переключения

git tag <имя метки> - теги. удобно в качестве ярлыка для хэша коммита


бесплатные приватные репозитории - bitbucket

"""













"""

+
+s6 = u'Unicode in Python 2'
+
+# bytes
+
+s7 = b'Hello' # <D0><B1><D0><B0><D0><B9><D1><82><D1><8B>, <D0><BF><D0><BE><D1><82><D0><BE><D0><BA> <D0><B4><D0><B0>
<D0><BD><D0><BD><D1><8B><D1><85> <D0><B1><D0><B5><D0><B7> <D0><BA><D0><BE><D0><B4><D0><B8><D1><80><D0><BE><D0><B2>
<D0><BA><D0><B8>
\ No newline at end of file

D:\py_bin>git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        lesson_2/

nothing added to commit but untracked files present (use "git add" to track)

D:\py_bin>git log
commit 9a490fbce944580544aaeed5c5eb20f0384300b2 (HEAD -> master)
Author: kvomelchuk <konstantin.omelchuk@gmail.com>
Date:   Fri Apr 13 19:43:43 2018 +0300

    <D0>D0><B5><D0><BA><D1><86><D0><B8><D1><8F> 1 <D1><87>.1

D:\py_bin>git add lesson_2/step_2.py

D:\py_bin>git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   lesson_2/step_2.py


D:\py_bin>git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   lesson_2/step_2.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        lesson_2/test.txt


D:\py_bin>git add lesson_2/test.txt

D:\py_bin>git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   lesson_2/step_2.py
        new file:   lesson_2/test.txt


D:\py_bin>git commit -m "second commit to repo"
[master 43d8db2] second commit to repo
 2 files changed, 46 insertions(+)
 create mode 100644 lesson_2/step_2.py
 create mode 100644 lesson_2/test.txt

D:\py_bin>git status
On branch master
nothing to commit, working tree clean

D:\py_bin>git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   lesson_2/test.txt

no changes added to commit (use "git add" and/or "git commit -a")

D:\py_bin>git checkout test.txt
error: pathspec 'test.txt' did not match any file(s) known to git.

D:\py_bin>git checkout lesson_2/test.txt

D:\py_bin>git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   lesson_2/test.txt

no changes added to commit (use "git add" and/or "git commit -a")

D:\py_bin>git add test.txt
fatal: pathspec 'test.txt' did not match any files

D:\py_bin>cd lesson_2

D:\py_bin\lesson_2>git test_2.txt
git: 'test_2.txt' is not a git command. See 'git --help'.

D:\py_bin\lesson_2>git add test_2.txt
fatal: pathspec 'test_2.txt' did not match any files

D:\py_bin\lesson_2>git add test.txt

D:\py_bin\lesson_2>git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   test.txt


D:\py_bin\lesson_2>git reset HEAD test.txt
Unstaged changes after reset:
M       lesson_2/test.txt

D:\py_bin\lesson_2>git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   test.txt

no changes added to commit (use "git add" and/or "git commit -a")

D:\py_bin\lesson_2>git status

D:\py_bin\lesson_2>
