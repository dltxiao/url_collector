# -*- coding: utf-8 -*-

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import mysql.connector
from db2xlsx import export_xlsx

DATABASE = 'url_collector'
DB_USER = 'zhong'
DB_PASS = 'xiao'
SECRET_KEY = 'zhongxiao'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return mysql.connector.connect(user='zhong', password='xiao', database='url_collector')

def pagenum(datalist, pageid):
    display_num = 50
    page_max = len(datalist)/display_num+1
    start_num = (pageid - 1)*display_num
    end_num = pageid * display_num
    return (page_max, start_num, end_num, len(datalist))

#每个请求的前置处理，连接数据库
@app.before_request
def before_request():
    g.db = connect_db()
    g.cursor = g.db.cursor()

#每个请求的后置处理，关闭数据库连接
@app.teardown_request
def teardown_request(exception):
    g.cursor.close()

#首页
@app.route('/', methods = ['GET', 'POST'])
def index():
    session['anonymous']=True
    '''
    g.cursor.execute('select domain,sub_class_id from urls order by second asc limit 10 ')
    domains = [dict(url=row[0], classid=row[1]) for row in g.cursor.fetchall()]
    print domains
    g.cursor.execute('select id,name from sub_class order by id asc')
    classes = [dict(id=row[0], name=row[1]) for row in g.cursor.fetchall()]
    return render_template('view_all.html', domains = domains, classes = classes)
    '''
    return render_template('layout.html')

#已分类URL页面
@app.route('/classified/', methods = ['GET', 'POST'])
@app.route('/classified/<int:pageid>', methods = ['GET', 'POST'])
def classified(pageid=1):
    g.cursor.execute('select domain,sub_class_id from urls where sub_class_id != 120 order by second asc')
    domains = [dict(url=row[0], classid=row[1]) for row in g.cursor.fetchall()]
    g.cursor.execute('select id,name from sub_class order by id asc')
    classes = [dict(id=row[0], name=row[1]) for row in g.cursor.fetchall()]
    pnum = pagenum(domains, pageid)
    update_count = 0

    if request.method == 'POST':
        input_ids = [row['url'] for row in domains[pnum[1]:pnum[2]]]
        select_ids = [row['url']+'_id' for row in domains[pnum[1]:pnum[2]]] 
        for input_id,select_id in zip(input_ids, select_ids):
            if dict(url=request.form[input_id], classid=int(request.form[select_id])) not in domains:
#                print 'update --> p1: %s' % dict(url=request.form[input_id], classid=request.form[select_id])
                g.cursor.execute('update urls set sub_class_id = %s where domain = %s',(request.form[select_id], request.form[input_id]))
                g.db.commit()
                update_count = update_count + 1
        flash('Update %d records!' % update_count)
        return redirect('/classified/')    
    if (pageid > 0 and pageid <= pnum[0]):
        return render_template('classified.html',pageid = pageid, page_max=pnum[0],total=pnum[3], domains = domains[pnum[1]:pnum[2]], classes = classes)
    else:
        flash('Invalid page')
        return redirect('/classified/')

#未分类URL页面
@app.route('/classifying/', methods = ['GET', 'POST'])
@app.route('/classifying/<int:pageid>', methods = ['GET', 'POST'])
def classifying(pageid=1):
    g.cursor.execute('select domain,sub_class_id from urls where sub_class_id = 120 order by second asc')
    domains = [dict(url=row[0], classid=row[1]) for row in g.cursor.fetchall()]
    g.cursor.execute('select id,name from sub_class order by id asc')
    classes = [dict(id=row[0], name=row[1]) for row in g.cursor.fetchall()]
    pnum = pagenum(domains, pageid)
    update_count = 0

    if request.method == 'POST':
        input_ids = [row['url'] for row in domains[pnum[1]:pnum[2]]]
        select_ids = [row['url']+'_id' for row in domains[pnum[1]:pnum[2]]]  
        for input_id,select_id in zip(input_ids, select_ids):
            if int(request.form[select_id]) != 120:
                print 'update --> p1: %s -- p2 %s' % (request.form[select_id], request.form[input_id])
                g.cursor.execute('update urls set sub_class_id = %s where domain = %s',(request.form[select_id], request.form[input_id]))
                g.db.commit()
                update_count = update_count + 1
        flash('Update %d records!' % update_count )
        return redirect('/classifying/')
    if (pageid > 0 and pageid <= pnum[0]):
        return render_template('classifying.html',pageid = pageid, page_max=pnum[0],total=pnum[3], domains = domains[pnum[1]:pnum[2]], classes = classes)
    else:
        flash('Invalid page')
        return redirect('/classifying/')

@app.route('/export', methods = ['GET'])
def export():
    g.cursor.execute('select domain,sub_class_id from urls where sub_class_id != 120 order by second asc')
    classfied_urls = [dict(url=row[0], classid=row[1]) for row in g.cursor.fetchall()]
    g.cursor.execute('select domain,sub_class_id from urls where sub_class_id = 120 order by second asc')
    classfying_urls = [dict(url=row[0], classid=row[1]) for row in g.cursor.fetchall()]
    export_xlsx(classfied_urls, classfying_urls)
    flash('export test!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(
        host='0.0.0.0'
    )