from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__,static_url_path='/static')
# Your database configuration
db = {
    'host': 'localhost',
    'username': 'root',
    'password': 'Suppi@789',
    'database': 'main'
}
def execute_query(query):
    sql = mysql.connector.connect(**db)
    cursor = sql.cursor()    
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    sql.close()
    return results

def execute_queryy19(queries2):
    sql = mysql.connector.connect(**db)
    cursor = sql.cursor()
    cursor.execute(queries2)
    results = cursor.fetchall()
    cursor.close()
    sql.close()
    return results

sql = mysql.connector.connect(**db)
cur = sql.cursor()

# Function to execute the SQL query and return results
@app.route("/")
def index():
    return render_template("index.html")
@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/dept')
def dept():
    return render_template('Dept.html')

@app.route('/alumni')
def alumni():
    return render_template('Alumni.html')

@app.route('/facilities')
def facilities():
    return render_template('facilities.html')

@app.route('/gallery')
def gallery():
    return render_template('Gallery.html')
@app.route('/placements')
def placements():
    return render_template('Placements.html')

@app.route('/query')
def query():
    return render_template('queries.html')

@app.route('/queries2')
def queries2():
    return render_template("queries2.html")

@app.route('/execute_query', methods=['POST', 'GET'])
def execute_query():
    if request.method == 'POST':
        query_type = request.form.get('query1')
        results = []
        results1 = []
        results2 = []
        results3 = []
        results4 = []
        results5 = []
        results6 = []
        results7 = []
        results8 = []
        if query_type == 'list_y20_students':
            query = """
            SELECT t1.regdno, t1.name AS name_table1,
                   t1.pd1 AS pd1_table1,  
                   t1.pd2 AS pd2_table1, 
                   t1.pd3 AS pd3_table1, 
                   t1.pd4 AS pd4_table1, 
                   t1.pd5 AS pd5_table1,  
                   t1.pd6 AS pd6_table1,
                   t1.pd7 AS pd7_table1,
                   t2.pd1 AS pd1_table2, 
                   t2.pd2 AS pd2_table2,
                   t2.pd3 AS pd3_table2, 
                   t2.pd4 AS pd4_table2,
                   t2.pd5 AS pd5_table2, 
                   t2.pd6 AS pd6_table2,
                   t2.pd7 AS pd7_table2,
                   t2.pd8 AS pd8_table2,
                   t2.pd9 AS pd9_table2,
                   t3.pd1 AS pd1_table3,  
                   t3.pd2 AS pd2_table3, 
                   t3.pd3 AS pd3_table3,  
                   t3.pd4 AS pd4_table3, 
                   t3.pd5 AS pd5_table3,
                   t3.pd6 AS pd6_table3, 
                   t3.pd7 AS pd7_table3, 
                   t3.pd8 AS pd8_table3, 
                   t3.pd9 AS pd9_table3, 
                   t4.pd1 AS pd1_table4, 
                   t4.pd2 AS pd2_table4,
                   t4.pd3 AS pd3_table4, 
                   t4.pd4 AS pd4_table4,
                   t4.pd5 AS pd5_table4, 
                   t4.pd6 AS pd6_table4,
                   t4.pd7 AS pd7_table4,
                   t4.pd8 AS pd8_table4,
                   t4.pd9 AS pd9_table4,
                   t5.pd1 AS pd1_table5,  
                   t5.pd2 AS pd2_table5, 
                   t5.pd3 AS pd3_table5,
                   t5.pd4 AS pd4_table5,
                   t5.pd5 AS pd5_table5, 
                   t5.pd6 AS pd6_table5,
                   t5.pd7 AS pd7_table5,
                   t5.pd8 AS pd8_table5, 
                   t5.pd9 AS pd9_table5, 
                   t5.pd10 AS pd10_table5, 
                   t5.pd11 AS pd11_table5,
                   t6.pd1 AS pd1_table6, 
                   t6.pd2 AS pd2_table6,
                   t6.pd3 AS pd3_table6, 
                   t6.pd4 AS pd4_table6,
                   t6.pd5 AS pd5_table6, 
                   t6.pd6 AS pd6_table6,
                   t6.pd7 AS pd7_table6,
                   t6.pd8 AS pd8_table6,
                   t6.pd9 AS pd9_table6,
                   t6.pd10 AS pd10_table6
                  FROM r20s11 t1
                JOIN r20s12 t2 ON t1.regdno = t2.regdno
                JOIN r20s21 t3 ON t1.regdno = t3.regdno
                JOIN r20s22 t4 ON t3.regdno = t4.regdno
                JOIN r20s31 t5 ON t4.regdno = t5.regdno
                JOIN r20s32 t6 ON t5.regdno = t6.regdno
                where (t1.pd1 = 'Jul-21' OR t1.pd1 IS NULL)
                AND (t1.pd2 = 'Jul-21' OR t1.pd2 IS NULL)AND (t1.pd3 = 'Jul-21' OR t1.pd3 IS NULL)
                AND (t1.pd4 = 'Jul-21' OR t1.pd4 IS NULL)AND (t1.pd5 = 'Jul-21' OR t1.pd5 IS NULL)
                AND (t1.pd6 = 'Jul-21' OR t1.pd6 IS NULL)AND (t1.pd7 = 'Jul-21' OR t1.pd7 IS NULL)
                AND (t2.pd1 = 'Oct-21' OR t2.pd1 IS NULL)AND (t2.pd2 = 'Oct-21' OR t2.pd2 IS NULL)
                AND (t2.pd3 = 'Oct-21' OR t2.pd3 IS NULL)AND (t2.pd4 = 'Oct-21' OR t2.pd4 IS NULL)
                AND (t2.pd5 = 'Oct-21' OR t2.pd5 IS NULL)AND (t2.pd6 = 'Oct-21' OR t2.pd6 IS NULL)
                AND (t2.pd7 = 'Oct-21' OR t2.pd7 IS NULL)AND (t2.pd8 = 'Oct-21' OR t2.pd8 IS NULL)
                AND (t2.pd9 = 'Oct-21' OR t2.pd9 IS NULL)
                AND t3.pd1 = 'Mar-22' AND t3.pd2 = 'Mar-22' AND t3.pd3 = 'Mar-22' AND t3.pd4 = 'Mar-22' AND t3.pd5 = 'Mar-22' AND t3.pd6 = 'Mar-22' AND t3.pd7 = 'Mar-22' AND t3.pd8 = 'Mar-22' AND t3.pd9 = 'Mar-22'
                AND t4.pd1 = 'Aug-22' AND t4.pd2 = 'Aug-22' AND t4.pd3 = 'Aug-22' AND t4.pd4 = 'Aug-22' AND t4.pd5 = 'Aug-22' AND t4.pd6 = 'Aug-22' AND t4.pd7 = 'Aug-22' AND t4.pd8 = 'Aug-22' 
                AND t5.pd1 = 'Feb-23' AND t5.pd2 = 'Feb-23' AND t5.pd3 = 'Feb-23' AND t5.pd4 = 'Feb-23' AND t5.pd5 = 'Feb-23' AND t5.pd6 = 'Feb-23' AND t5.pd7 = 'Feb-23' AND t5.pd8 = 'Feb-23' AND t5.pd9 = 'Feb-23' AND t5.pd10 = 'Feb-23' 
                AND t6.pd1 = 'Aug-23' AND t6.pd2 = 'Aug-23' AND t6.pd3 = 'Aug-23' AND t6.pd4 = 'Aug-23' AND t6.pd5 = 'Aug-23' AND t6.pd6 = 'Aug-23' AND t6.pd7 = 'Aug-23' AND t6.pd8 = 'Aug-23' AND t6.pd9 = 'Aug-23';
                """
            cur.execute(query)
            results.extend(cur.fetchall())
            return render_template('Gallery.html', results=results)

        elif query_type == 'list_students_with_backlogs':
            query = """SELECT 
                   t1.regdno,
                   t1.name AS name_table1,
                   SUM(
                   CASE WHEN t1.pd1 = '-' THEN 1 ELSE 0 END +
                   CASE WHEN t1.pd2 = '-' THEN 1 ELSE 0 END +
                   CASE WHEN t1.pd3 = '-' THEN 1 ELSE 0 END +
                   CASE WHEN t1.pd4 = '-' THEN 1 ELSE 0 END +
                   CASE WHEN t1.pd5 = '-' THEN 1 ELSE 0 END +
                  CASE WHEN t1.pd6 = '-' THEN 1 ELSE 0 END +
                  CASE WHEN t1.pd7 = '-' THEN 1 ELSE 0 END +
                  CASE WHEN t1.pd8 = '-' THEN 1 ELSE 0 END
                  ) AS backlog_count_t1,
                   SUM(
                   CASE WHEN t2.pd1 = '-' THEN 1 ELSE 0 END +
                   CASE WHEN t2.pd2 = '-' THEN 1 ELSE 0 END +
                   CASE WHEN t2.pd3 = '-' THEN 1 ELSE 0 END +
                   CASE WHEN t2.pd4 = '-' THEN 1 ELSE 0 END +
                   CASE WHEN t2.pd5 = '-' THEN 1 ELSE 0 END +
                   CASE WHEN t2.pd6 = '-' THEN 1 ELSE 0 END +
                    CASE WHEN t2.pd7 = '-' THEN 1 ELSE 0 END +
                   CASE WHEN t2.pd8 = '-' THEN 1 ELSE 0 END +
                  CASE WHEN t2.pd9 = '-' THEN 1 ELSE 0 END
                  ) AS backlog_count_t2,
                  SUM(
                     CASE WHEN t3.pd1 = '-' THEN 1 ELSE 0 END +
                     CASE WHEN t3.pd2 = '-' THEN 1 ELSE 0 END +
                     CASE WHEN t3.pd3 = '-' THEN 1 ELSE 0 END +
                     CASE WHEN t3.pd4 = '-' THEN 1 ELSE 0 END +
                     CASE WHEN t3.pd5 = '-' THEN 1 ELSE 0 END +
                     CASE WHEN t3.pd6 = '-' THEN 1 ELSE 0 END +
                     CASE WHEN t3.pd7 = '-' THEN 1 ELSE 0 END +
                     CASE WHEN t3.pd8 = '-' THEN 1 ELSE 0 END +
                     CASE WHEN t3.pd9 = '-' THEN 1 ELSE 0 END
                   ) AS backlog_count_t3,
                   SUM(
                        CASE WHEN t4.pd1 = '-' THEN 1 ELSE 0 END +
                        CASE WHEN t4.pd2 = '-' THEN 1 ELSE 0 END +
                       CASE WHEN t4.pd3 = '-' THEN 1 ELSE 0 END +
                      CASE WHEN t4.pd4 = '-' THEN 1 ELSE 0 END +
                         CASE WHEN t4.pd5 = '-' THEN 1 ELSE 0 END +
                         CASE WHEN t4.pd6 = '-' THEN 1 ELSE 0 END +
                         CASE WHEN t4.pd7 = '-' THEN 1 ELSE 0 END +
                         CASE WHEN t4.pd8 = '-' THEN 1 ELSE 0 END +
                            CASE WHEN t4.pd9 = '-' THEN 1 ELSE 0 END
                          ) AS backlog_count_t4,
                          SUM(
                                  CASE WHEN t5.pd1 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t5.pd2 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t5.pd3 = '-' THEN 1 ELSE 0 END +
                                 CASE WHEN t5.pd4 = '-' THEN 1 ELSE 0 END +
                                 CASE WHEN t5.pd5 = '-' THEN 1 ELSE 0 END +
                                 CASE WHEN t5.pd6 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t5.pd7 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t5.pd8 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t5.pd9 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t5.pd10 = '-' THEN 1 ELSE 0 END
                                 ) AS backlog_count_t5,
                             SUM(
                              CASE WHEN t6.pd1 = '-' THEN 1 ELSE 0 END +
                              CASE WHEN t6.pd2 = '-' THEN 1 ELSE 0 END +
                              CASE WHEN t6.pd3 = '-' THEN 1 ELSE 0 END +
                              CASE WHEN t6.pd4 = '-' THEN 1 ELSE 0 END +
                              CASE WHEN t6.pd5 = '-' THEN 1 ELSE 0 END +
                              CASE WHEN t6.pd6 = '-' THEN 1 ELSE 0 END +
                              CASE WHEN t6.pd7 = '-' THEN 1 ELSE 0 END +
                              CASE WHEN t6.pd8 = '-' THEN 1 ELSE 0 END +
                              CASE WHEN t6.pd9 = '-' THEN 1 ELSE 0 END +
                              CASE WHEN t6.pd10 = '-' THEN 1 ELSE 0 END
                              ) AS backlog_count_t6,
                         SUM(
                           CASE WHEN t1.pd1 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t1.pd2 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t1.pd3 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t1.pd4 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t1.pd5 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t1.pd6 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t1.pd7 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t2.pd1 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t2.pd2 = '-' THEN 1 ELSE 0 END +
                            CASE WHEN t2.pd3 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t2.pd4 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t2.pd5 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t2.pd6 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t2.pd7 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t2.pd8 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t2.pd9 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t3.pd1 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t3.pd2 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t3.pd3 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t3.pd4 = '-' THEN 1 ELSE 0 END +
                            CASE WHEN t3.pd5 = '-' THEN 1 ELSE 0 END +
                            CASE WHEN t3.pd6 = '-' THEN 1 ELSE 0 END +
                            CASE WHEN t3.pd7 = '-' THEN 1 ELSE 0 END +
                            CASE WHEN t3.pd8 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t3.pd9 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t4.pd1 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t4.pd2 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t4.pd3 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t4.pd4 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t4.pd5 = '-' THEN 1 ELSE 0 END +
                           CASE WHEN t4.pd6 = '-' THEN 1 ELSE 0 END +
                            CASE WHEN t4.pd7 = '-' THEN 1 ELSE 0 END +
                            CASE WHEN t4.pd8 = '-' THEN 1 ELSE 0 END +
                            CASE WHEN t4.pd9 = '-' THEN 1 ELSE 0 END +
                            CASE WHEN t5.pd1 = '-' THEN 1 ELSE 0 END +
                             CASE WHEN t5.pd2 = '-' THEN 1 ELSE 0 END +
                             CASE WHEN t5.pd3 = '-' THEN 1 ELSE 0 END +
                              CASE WHEN t5.pd4 = '-' THEN 1 ELSE 0 END +
                             CASE WHEN t5.pd5 = '-' THEN 1 ELSE 0 END +
                             CASE WHEN t5.pd6 = '-' THEN 1 ELSE 0 END +
                             CASE WHEN t5.pd7 = '-' THEN 1 ELSE 0 END +
                              CASE WHEN t5.pd8 = '-' THEN 1 ELSE 0 END +
                             CASE WHEN t5.pd9 = '-' THEN 1 ELSE 0 END +
                              CASE WHEN t5.pd10 = '-' THEN 1 ELSE 0 END +
                              CASE WHEN t6.pd1 = '-' THEN 1 ELSE 0 END +
                              CASE WHEN t6.pd2 = '-' THEN 1 ELSE 0 END +
                              CASE WHEN t6.pd3 = '-' THEN 1 ELSE 0 END +
                              CASE WHEN t6.pd4 = '-' THEN 1 ELSE 0 END +
                              CASE WHEN t6.pd5 = '-' THEN 1 ELSE 0 END +
                              CASE WHEN t6.pd6 = '-' THEN 1 ELSE 0 END +
                              CASE WHEN t6.pd7 = '-' THEN 1 ELSE 0 END +
                              CASE WHEN t6.pd8 = '-' THEN 1 ELSE 0 END +
                              CASE WHEN t6.pd9 = '-' THEN 1 ELSE 0 END +
                              CASE WHEN t6.pd10 = '-' THEN 1 ELSE 0 END 
                           ) AS total_backlog_sum
                                     FROM 
                                r20s11 t1
                            JOIN 
                                r20s12 t2 ON t1.regdno = t2.regdno
                            JOIN 
                                 r20s21 t3 ON t1.regdno = t3.regdno
                            JOIN 
                                  r20s22 t4 ON t3.regdno = t4.regdno
                            JOIN 
                                 r20s31 t5 ON t4.regdno = t5.regdno
                            JOIN 
                                r20s32 t6 ON t5.regdno = t6.regdno
                                WHERE 
                               t1.pd1 = '-' OR t1.pd2 = '-' OR t1.pd3 = '-' OR t1.pd4 = '-' OR t1.pd5 = '-' OR t1.pd6 = '-' OR t1.pd7 = '-' OR 
                               t2.pd1 = '-' OR t2.pd2 = '-' OR t2.pd3 = '-' OR t2.pd4 = '-' OR t2.pd5 = '-' OR t2.pd6 = '-' OR t2.pd7 = '-' OR t2.pd8 = '-' OR t2.pd9 = '-' OR
                               t3.pd1 = '-' OR t3.pd2 = '-' OR t3.pd3 = '-' OR t3.pd4 = '-' OR t3.pd5 = '-' OR t3.pd6 = '-' OR t3.pd7 = '-' OR t3.pd8 = '-' OR t3.pd9 = '-' OR
                               t4.pd1 = '-' OR t4.pd2 = '-' OR t4.pd3 = '-' OR t4.pd4 = '-' OR t4.pd5 = '-' OR t4.pd6 = '-' OR t4.pd7 = '-' OR t4.pd8 = '-' OR t4.pd9 = '-' OR
                                t5.pd1 = '-' OR t5.pd2 = '-' OR t5.pd3 = '-' OR t5.pd4 = '-' OR t5.pd5 = '-' OR t5.pd6 = '-' OR t5.pd7 = '-' OR t5.pd8 = '-' OR t5.pd9 = '-' OR t5.pd10 = '-' OR
                               t6.pd1 = '-' OR t6.pd2 = '-' OR t6.pd3 = '-' OR t6.pd4 = '-' OR t6.pd5 = '-' OR t6.pd6 = '-' OR t6.pd7 = '-' OR t6.pd8 = '-' OR t6.pd9 = '-' OR t6.pd10 = '-' 
                              GROUP BY 
                              t1.regdno, 
                              t1.name
                             LIMIT 1000;"""
            cur.execute(query)
            results1.extend(cur.fetchall())
            return render_template('backlogs.html', results1=results1)

        elif query_type == "negative_trend_backlogs":
              query="""SELECT * FROM (       
                                 SELECT 
                                 t1.regdno,
                                 t1.name AS name_table1,
                              SUM(
                                   CASE WHEN t1.pd1 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t1.pd2 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t1.pd3 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t1.pd4 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t1.pd5 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t1.pd6 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t1.pd7 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t1.pd8 = '-' THEN 1 ELSE 0 END
                                ) AS backlog_count_t1,
                                 SUM(
                                CASE WHEN t2.pd1 = '-' THEN 1 ELSE 0 END +
                                CASE WHEN t2.pd2 = '-' THEN 1 ELSE 0 END +
                                CASE WHEN t2.pd3 = '-' THEN 1 ELSE 0 END +
                                CASE WHEN t2.pd4 = '-' THEN 1 ELSE 0 END +
                                CASE WHEN t2.pd5 = '-' THEN 1 ELSE 0 END +
                                CASE WHEN t2.pd6 = '-' THEN 1 ELSE 0 END +
                                CASE WHEN t2.pd7 = '-' THEN 1 ELSE 0 END +
                                CASE WHEN t2.pd8 = '-' THEN 1 ELSE 0 END +
                                CASE WHEN t2.pd9 = '-' THEN 1 ELSE 0 END
                               ) AS backlog_count_t2,
                               SUM(
                                  CASE WHEN t3.pd1 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t3.pd2 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t3.pd3 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t3.pd4 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t3.pd5 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t3.pd6 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t3.pd7 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t3.pd8 = '-' THEN 1 ELSE 0 END +
                                 CASE WHEN t3.pd9 = '-' THEN 1 ELSE 0 END
                                ) AS backlog_count_t3,
                                  SUM(
                                    CASE WHEN t4.pd1 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t4.pd2 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t4.pd3 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t4.pd4 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t4.pd5 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t4.pd6 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t4.pd7 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t4.pd8 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t4.pd9 = '-' THEN 1 ELSE 0 END
                                     ) AS backlog_count_t4,
                                      SUM(
                                     CASE WHEN t5.pd1 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t5.pd2 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t5.pd3 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t5.pd4 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t5.pd5 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t5.pd6 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t5.pd7 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t5.pd8 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t5.pd9 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t5.pd10 = '-' THEN 1 ELSE 0 END
                                ) AS backlog_count_t5,
                                      SUM(
                                     CASE WHEN t6.pd1 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t6.pd2 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t6.pd3 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t6.pd4 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t6.pd5 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t6.pd6 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t6.pd7 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t6.pd8 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t6.pd9 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t6.pd10 = '-' THEN 1 ELSE 0 END
                                    ) AS backlog_count_t6,
                                        SUM(
                                    CASE WHEN t1.pd1 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t1.pd2 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t1.pd3 = '-' THEN 1 ELSE 0 END +
                                       CASE WHEN t1.pd4 = '-' THEN 1 ELSE 0 END +
                                       CASE WHEN t1.pd5 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t1.pd6 = '-' THEN 1 ELSE 0 END +
                                         CASE WHEN t1.pd7 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t2.pd1 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t2.pd2 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t2.pd3 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t2.pd4 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t2.pd5 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t2.pd6 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t2.pd7 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t2.pd8 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t2.pd9 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t3.pd1 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t3.pd2 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t3.pd3 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t3.pd4 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t3.pd5 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t3.pd6 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t3.pd7 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t3.pd8 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t3.pd9 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t4.pd1 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t4.pd2 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t4.pd3 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t4.pd4 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t4.pd5 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t4.pd6 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t4.pd7 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t4.pd8 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t4.pd9 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t5.pd1 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t5.pd2 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t5.pd3 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t5.pd4 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t5.pd5 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t5.pd6 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t5.pd7 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t5.pd8 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t5.pd9 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t5.pd10 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t6.pd1 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t6.pd2 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t6.pd3 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t6.pd4 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t6.pd5 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t6.pd6 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t6.pd7 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t6.pd8 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t6.pd9 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t6.pd10 = '-' THEN 1 ELSE 0 END 
                                ) AS total_backlog_sum
                                   FROM 
                                     r20s11 t1
                                JOIN 
                                  r20s12 t2 ON t1.regdno = t2.regdno
                                JOIN 
                                  r20s21 t3 ON t1.regdno = t3.regdno
                                JOIN 
                                 r20s22 t4 ON t3.regdno = t4.regdno
                                JOIN 
                                 r20s31 t5 ON t4.regdno = t5.regdno
                                JOIN 
                                r20s32 t6 ON t5.regdno = t6.regdno
                                  WHERE 
                                 t1.pd1 = '-' OR t1.pd2 = '-' OR t1.pd3 = '-' OR t1.pd4 = '-' OR t1.pd5 = '-' OR t1.pd6 = '-' OR t1.pd7 = '-' OR 
                                 t2.pd1 = '-' OR t2.pd2 = '-' OR t2.pd3 = '-' OR t2.pd4 = '-' OR t2.pd5 = '-' OR t2.pd6 = '-' OR t2.pd7 = '-' OR t2.pd8 = '-' OR t2.pd9 = '-' OR
                                 t3.pd1 = '-' OR t3.pd2 = '-' OR t3.pd3 = '-' OR t3.pd4 = '-' OR t3.pd5 = '-' OR t3.pd6 = '-' OR t3.pd7 = '-' OR t3.pd8 = '-' OR t3.pd9 = '-' OR
                                 t4.pd1 = '-' OR t4.pd2 = '-' OR t4.pd3 = '-' OR t4.pd4 = '-' OR t4.pd5 = '-' OR t4.pd6 = '-' OR t4.pd7 = '-' OR t4.pd8 = '-' OR t4.pd9 = '-' OR
                                t5.pd1 = '-' OR t5.pd2 = '-' OR t5.pd3 = '-' OR t5.pd4 = '-' OR t5.pd5 = '-' OR t5.pd6 = '-' OR t5.pd7 = '-' OR t5.pd8 = '-' OR t5.pd9 = '-' OR t5.pd10 = '-' OR
                                t6.pd1 = '-' OR t6.pd2 = '-' OR t6.pd3 = '-' OR t6.pd4 = '-' OR t6.pd5 = '-' OR t6.pd6 = '-' OR t6.pd7 = '-' OR t6.pd8 = '-' OR t6.pd9 = '-' OR t6.pd10 = '-' 
                           GROUP BY 
                             t1.regdno, 
                              t1.name
                            ) AS subquery
                                 WHERE 
                              backlog_count_t1 > backlog_count_t2 AND
                              backlog_count_t2 > backlog_count_t3 AND
                              backlog_count_t3 > backlog_count_t4 AND
                              backlog_count_t4 > backlog_count_t5 AND
                              backlog_count_t5 > backlog_count_t6 
                               ORDER BY 
                                total_backlog_sum; """
              cur.execute(query)
              results2.extend(cur.fetchall())
              return render_template('backlogs negative trend.html',results2=results2)

        elif query_type == "positive_trend_backlogs":
            query="""SELECT * FROM (       
                                 SELECT 
                                 t1.regdno,
                                 t1.name AS name_table1,
                              SUM(
                                   CASE WHEN t1.pd1 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t1.pd2 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t1.pd3 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t1.pd4 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t1.pd5 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t1.pd6 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t1.pd7 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t1.pd8 = '-' THEN 1 ELSE 0 END
                                ) AS backlog_count_t1,
                                 SUM(
                                CASE WHEN t2.pd1 = '-' THEN 1 ELSE 0 END +
                                CASE WHEN t2.pd2 = '-' THEN 1 ELSE 0 END +
                                CASE WHEN t2.pd3 = '-' THEN 1 ELSE 0 END +
                                CASE WHEN t2.pd4 = '-' THEN 1 ELSE 0 END +
                                CASE WHEN t2.pd5 = '-' THEN 1 ELSE 0 END +
                                CASE WHEN t2.pd6 = '-' THEN 1 ELSE 0 END +
                                CASE WHEN t2.pd7 = '-' THEN 1 ELSE 0 END +
                                CASE WHEN t2.pd8 = '-' THEN 1 ELSE 0 END +
                                CASE WHEN t2.pd9 = '-' THEN 1 ELSE 0 END
                               ) AS backlog_count_t2,
                               SUM(
                                  CASE WHEN t3.pd1 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t3.pd2 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t3.pd3 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t3.pd4 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t3.pd5 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t3.pd6 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t3.pd7 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t3.pd8 = '-' THEN 1 ELSE 0 END +
                                 CASE WHEN t3.pd9 = '-' THEN 1 ELSE 0 END
                                ) AS backlog_count_t3,
                                  SUM(
                                    CASE WHEN t4.pd1 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t4.pd2 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t4.pd3 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t4.pd4 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t4.pd5 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t4.pd6 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t4.pd7 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t4.pd8 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t4.pd9 = '-' THEN 1 ELSE 0 END
                                     ) AS backlog_count_t4,
                                      SUM(
                                     CASE WHEN t5.pd1 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t5.pd2 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t5.pd3 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t5.pd4 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t5.pd5 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t5.pd6 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t5.pd7 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t5.pd8 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t5.pd9 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t5.pd10 = '-' THEN 1 ELSE 0 END
                                ) AS backlog_count_t5,
                                      SUM(
                                     CASE WHEN t6.pd1 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t6.pd2 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t6.pd3 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t6.pd4 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t6.pd5 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t6.pd6 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t6.pd7 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t6.pd8 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t6.pd9 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t6.pd10 = '-' THEN 1 ELSE 0 END
                                    ) AS backlog_count_t6,
                                        SUM(
                                    CASE WHEN t1.pd1 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t1.pd2 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t1.pd3 = '-' THEN 1 ELSE 0 END +
                                       CASE WHEN t1.pd4 = '-' THEN 1 ELSE 0 END +
                                       CASE WHEN t1.pd5 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t1.pd6 = '-' THEN 1 ELSE 0 END +
                                        CASE WHEN t1.pd7 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t2.pd1 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t2.pd2 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t2.pd3 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t2.pd4 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t2.pd5 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t2.pd6 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t2.pd7 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t2.pd8 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t2.pd9 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t3.pd1 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t3.pd2 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t3.pd3 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t3.pd4 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t3.pd5 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t3.pd6 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t3.pd7 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t3.pd8 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t3.pd9 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t4.pd1 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t4.pd2 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t4.pd3 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t4.pd4 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t4.pd5 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t4.pd6 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t4.pd7 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t4.pd8 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t4.pd9 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t5.pd1 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t5.pd2 = '-' THEN 1 ELSE 0 END +
                                      CASE WHEN t5.pd3 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t5.pd4 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t5.pd5 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t5.pd6 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t5.pd7 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t5.pd8 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t5.pd9 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t5.pd10 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t6.pd1 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t6.pd2 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t6.pd3 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t6.pd4 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t6.pd5 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t6.pd6 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t6.pd7 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t6.pd8 = '-' THEN 1 ELSE 0 END +
                                    CASE WHEN t6.pd9 = '-' THEN 1 ELSE 0 END +
                                     CASE WHEN t6.pd10 = '-' THEN 1 ELSE 0 END 
                                ) AS total_backlog_sum
                                   FROM 
                                     r20s11 t1
                                JOIN 
                                  r20s12 t2 ON t1.regdno = t2.regdno
                                JOIN 
                                  r20s21 t3 ON t1.regdno = t3.regdno
                                JOIN 
                                 r20s22 t4 ON t3.regdno = t4.regdno
                                JOIN 
                                 r20s31 t5 ON t4.regdno = t5.regdno
                                JOIN 
                                r20s32 t6 ON t5.regdno = t6.regdno
                                  WHERE 
                                 t1.pd1 = '-' OR t1.pd2 = '-' OR t1.pd3 = '-' OR t1.pd4 = '-' OR t1.pd5 = '-' OR t1.pd6 = '-' OR t1.pd7 = '-' OR 
                                 t2.pd1 = '-' OR t2.pd2 = '-' OR t2.pd3 = '-' OR t2.pd4 = '-' OR t2.pd5 = '-' OR t2.pd6 = '-' OR t2.pd7 = '-' OR t2.pd8 = '-' OR t2.pd9 = '-' OR
                                 t3.pd1 = '-' OR t3.pd2 = '-' OR t3.pd3 = '-' OR t3.pd4 = '-' OR t3.pd5 = '-' OR t3.pd6 = '-' OR t3.pd7 = '-' OR t3.pd8 = '-' OR t3.pd9 = '-' OR
                                 t4.pd1 = '-' OR t4.pd2 = '-' OR t4.pd3 = '-' OR t4.pd4 = '-' OR t4.pd5 = '-' OR t4.pd6 = '-' OR t4.pd7 = '-' OR t4.pd8 = '-' OR t4.pd9 = '-' OR
                                t5.pd1 = '-' OR t5.pd2 = '-' OR t5.pd3 = '-' OR t5.pd4 = '-' OR t5.pd5 = '-' OR t5.pd6 = '-' OR t5.pd7 = '-' OR t5.pd8 = '-' OR t5.pd9 = '-' OR t5.pd10 = '-' OR
                                t6.pd1 = '-' OR t6.pd2 = '-' OR t6.pd3 = '-' OR t6.pd4 = '-' OR t6.pd5 = '-' OR t6.pd6 = '-' OR t6.pd7 = '-' OR t6.pd8 = '-' OR t6.pd9 = '-' OR t6.pd10 = '-' 
                           GROUP BY 
                             t1.regdno, 
                              t1.name
                            ) AS subquery
                                 WHERE 
                              backlog_count_t1 <= backlog_count_t2 AND
                              backlog_count_t2 <= backlog_count_t3 AND
                              backlog_count_t3 <= backlog_count_t4 AND
                              backlog_count_t4 <= backlog_count_t5 AND
                              backlog_count_t5 <= backlog_count_t6 
                               ORDER BY 
                                total_backlog_sum; """
            cur.execute(query)
            results3.extend(cur.fetchall())
            return render_template('backlogs positive trend.html',results3=results3)

        elif query_type == "negative_trend_sgpa":
            query="""
                       SELECT regdno,name_table1,sgpa_table1,sgpa_table2,sgpa_table3,sgpa_table4,sgpa_table5,sgpa_table6
                           FROM (
                       SELECT 
                       t1.regdno,t1.name AS name_table1,t1.sgpa AS sgpa_table1,t2.sgpa AS sgpa_table2,
                       t3.sgpa AS sgpa_table3,t4.sgpa AS sgpa_table4,t5.sgpa AS sgpa_table5,t6.sgpa AS sgpa_table6
                       FROM 
                       r20s11 t1
                       JOIN 
                          r20s12 t2 ON t1.regdno = t2.regdno
                       JOIN 
                          r20s21 t3 ON t1.regdno = t3.regdno
                       JOIN 
                          r20s22 t4 ON t3.regdno = t4.regdno
                       JOIN 
                          r20s31 t5 ON t4.regdno = t5.regdno
                        JOIN 
                           r20s32 t6 ON t5.regdno = t6.regdno
                       ) AS all_sgpa
                       WHERE 
                      sgpa_table1 > sgpa_table2 AND
                      sgpa_table2 > sgpa_table3 AND
                      sgpa_table3 > sgpa_table4 AND
                      sgpa_table4 > sgpa_table5 AND
                       sgpa_table5 > sgpa_table6 ;"""
            cur.execute(query)
            results4.extend(cur.fetchall())
            return render_template('SGPA negative trend.html', results4=results4)
        elif query_type == "positive_trend_sgpa":
            query="""
                       SELECT regdno,name_table1,sgpa_table1,sgpa_table2,sgpa_table3,sgpa_table4,sgpa_table5,sgpa_table6
                           FROM (
                       SELECT 
                       t1.regdno,t1.name AS name_table1,t1.sgpa AS sgpa_table1,t2.sgpa AS sgpa_table2,
                       t3.sgpa AS sgpa_table3,t4.sgpa AS sgpa_table4,t5.sgpa AS sgpa_table5,t6.sgpa AS sgpa_table6
                       FROM 
                       r20s11 t1
                       JOIN 
                          r20s12 t2 ON t1.regdno = t2.regdno
                       JOIN 
                          r20s21 t3 ON t1.regdno = t3.regdno
                       JOIN 
                          r20s22 t4 ON t3.regdno = t4.regdno
                       JOIN 
                          r20s31 t5 ON t4.regdno = t5.regdno
                        JOIN 
                           r20s32 t6 ON t5.regdno = t6.regdno
                       ) AS all_sgpa
                       WHERE 
                      sgpa_table1 <= sgpa_table2 AND
                      sgpa_table2 <= sgpa_table3 AND
                      sgpa_table3 <= sgpa_table4 AND
                      sgpa_table4 <= sgpa_table5 AND
                      sgpa_table5 <= sgpa_table6 ;"""
            cur.execute(query)
            results5.extend(cur.fetchall())
            return render_template('SGPA positive trend.html', results5=results5)
        elif query_type == "students_percentage_gt_75":
            query=""" 
            select regdno,name,percentage,gender from `y20percentage` where percentage>=75 ORDER BY percentage DESC;"""
            cur.execute(query)
            results6.extend(cur.fetchall())
            return render_template('percentage.html', results6=results6)

        elif query_type == "students_percentage_gt_75 who is male":
            query=""" select regdno,name,percentage,gender from `y20percentage` where percentage>=75 and gender="M" 
            ORDER BY percentage DESC; """
            cur.execute(query)
            results7.extend(cur.fetchall())
            return render_template('male percentage.html', results7=results7)
        elif query_type == "students_percentage_gt_75 who is female":
            query=""" select regdno,name,percentage,gender from `y20percentage` where percentage>=75 and gender="F" 
            ORDER BY percentage DESC; """
        cur.execute(query)
        results8.extend(cur.fetchall())
        return render_template('female percentage.html', results8=results8)

@app.route('/execute_queryy19', methods=['POST', 'GET'])
def execute_queryy19():
    if request.method == 'POST':
        query_type = request.form.get('query2')
        results = []
        results11 = []
        results2 = []
        results33 = []
        results4 = []
        results5 = []
        results6 = []
        results7 = []
        results8 = []
        if query_type == 'list_y19_students':
            query = """ SELECT t1.regdno, t1.name AS name_table1,t1.pd1 AS pd1_table1,t1.pd2 AS pd2_table1, 
                    t1.pd3 AS pd3_table1,t1.pd4 AS pd4_table1,t1.pd5 AS pd5_table1,t1.pd6 AS pd6_table1,
                    t1.pd7 AS pd7_table1,t1.pd8 AS pd8_table1,t2.pd1 AS pd1_table2,t2.pd2 AS pd2_table2,
                    t2.pd3 AS pd3_table2,t2.pd4 AS pd4_table2,t2.pd5 AS pd5_table2,t2.pd6 AS pd6_table2,
                    t2.pd7 AS pd7_table2,t2.pd8 AS pd8_table2,t2.pd9 AS pd9_table2,t3.pd1 AS pd1_table3,  
                    t3.pd2 AS pd2_table3,t3.pd3 AS pd3_table3,t3.pd4 AS pd4_table3,t3.pd5 AS pd5_table3,
                    t3.pd6 AS pd6_table3,t3.pd7 AS pd7_table3,t3.pd8 AS pd8_table3,t3.pd9 AS pd9_table3, 
                    t4.pd1 AS pd1_table4,t4.pd2 AS pd2_table4,t4.pd3 AS pd3_table4, t4.pd4 AS pd4_table4,
                    t4.pd5 AS pd5_table4, t4.pd6 AS pd6_table4,t4.pd7 AS pd7_table4,t4.pd8 AS pd8_table4,
                    t4.pd9 AS pd9_table4,t5.pd1 AS pd1_table5,t5.pd2 AS pd2_table5,t5.pd3 AS pd3_table5,
                    t5.pd4 AS pd4_table5,t5.pd5 AS pd5_table5,t5.pd6 AS pd6_table5,t5.pd7 AS pd7_table5,
                    t5.pd8 AS pd8_table5,t5.pd9 AS pd9_table5,t5.pd10 AS pd10_table5,t6.pd1 AS pd1_table6, 
                    t6.pd2 AS pd2_table6,t6.pd3 AS pd3_table6,t6.pd4 AS pd4_table6,t6.pd5 AS pd5_table6, 
                    t6.pd6 AS pd6_table6,t6.pd7 AS pd7_table6,t6.pd8 AS pd8_table6,t6.pd9 AS pd9_table6,
                    t7.pd1 AS pd1_table7,t7.pd2 AS pd2_table7,t7.pd3 AS pd3_table7,t7.pd4 AS pd4_table7,
                    t7.pd5 AS pd5_table7,t7.pd6 AS pd6_table7,t7.pd7 AS pd7_table7,t7.pd8 AS pd8_table7,
                    t7.pd9 AS pd9_table7,t7.pd10 AS pd10_table7,t8.pd1 AS pd1_table8,t8.pd2 AS pd2_table8,
                    t8.pd3 AS pd3_table8,t8.pd4 AS pd4_table8
                     FROM r18s11 t1
                     JOIN r18s12 t2 ON t1.regdno = t2.regdno
                     JOIN r18s21 t3 ON t1.regdno = t3.regdno
                     JOIN r18s22 t4 ON t3.regdno = t4.regdno
                     JOIN r18s31 t5 ON t4.regdno = t5.regdno
                     JOIN r18s32 t6 ON t5.regdno = t6.regdno
                     JOIN r18s41 t7 ON t6.regdno = t7.regdno
                     JOIN r18s42 t8 ON t7.regdno = t8.regdno
                     where (t1.pd1 = 'Nov-19' OR t1.pd1 IS NULL)
                    AND (t1.pd2 = 'Nov-19' OR t1.pd2 IS NULL)AND (t1.pd3 = 'Nov-19' OR t1.pd3 IS NULL)
                    AND (t1.pd4 = 'Nov-19' OR t1.pd4 IS NULL)AND (t1.pd5 = 'Nov-19' OR t1.pd5 IS NULL)
                    AND (t1.pd6 = 'Nov-19' OR t1.pd6 IS NULL)AND (t1.pd7 = 'Nov-19' OR t1.pd7 IS NULL)
                    AND (t1.pd8 = 'Nov-19' OR t1.pd7 IS NULL)
                    AND (t2.pd1 = 'Nov-20' OR t2.pd1 IS NULL)AND (t2.pd2 = 'Nov-20' OR t2.pd2 IS NULL)
                    AND (t2.pd3 = 'Nov-20' OR t2.pd3 IS NULL)AND (t2.pd4 = 'Nov-20' OR t2.pd4 IS NULL)
                    AND (t2.pd5 = 'Nov-20' OR t2.pd5 IS NULL)AND (t2.pd6 = 'Nov-20' OR t2.pd6 IS NULL)
                    AND (t2.pd7 = 'Nov-20' OR t2.pd7 IS NULL)AND (t2.pd8 = 'Nov-20' OR t2.pd8 IS NULL)
                    AND (t2.pd9 = 'Nov-20' OR t2.pd9 IS NULL)
                    AND t3.pd1 = 'Feb-21' AND t3.pd2 = 'Feb-21' AND t3.pd3 = 'Feb-21'  AND t3.pd4 = 'Feb-21'  AND t3.pd5 = 'Feb-21'  AND t3.pd6 = 'Feb-21'  AND t3.pd7 = 'Feb-21'  AND t3.pd8 = 'Feb-21'  AND t3.pd9 = 'Feb-21'
                    AND t4.pd1 = 'Aug-21' AND t4.pd2 = 'Aug-21' AND t4.pd3 = 'Aug-21' AND t4.pd4 = 'Aug-21' AND t4.pd5 = 'Aug-21' AND t4.pd6 = 'Aug-21' AND t4.pd7 = 'Aug-21' AND t4.pd8 = 'Aug-21' AND t4.pd9 = 'Aug-21'
                    AND t5.pd1 = 'Jan-22' AND t5.pd2 = 'Jan-22'  AND t5.pd3 = 'Jan-22'  AND t5.pd4 = 'Jan-22'  AND t5.pd5 = 'Jan-22'  AND t5.pd6 = 'Jan-22'  AND t5.pd7 = 'Jan-22'  AND t5.pd8 = 'Jan-22'  AND t5.pd9 = 'Jan-22'  AND t5.pd10 = 'Jan-22'  
                    AND t6.pd1 = 'Jun-22' AND t6.pd2 = 'Jun-22'  AND t6.pd3 = 'Jun-22' AND t6.pd4 = 'Jun-22' AND t6.pd5 = 'Jun-22' AND t6.pd6 = 'Jun-22' AND t6.pd7 = 'Jun-22' AND t6.pd8 = 'Jun-22' AND t6.pd9 ='Jun-22'
                    AND t7.pd1 = 'Nov-22' AND t7.pd2 = 'Nov-22'  AND t7.pd3 = 'Nov-22'  AND t7.pd4 = 'Nov-22' AND t7.pd5 = 'Nov-22' AND t7.pd6 = 'Nov-22' AND t7.pd7 = 'Nov-22' AND t7.pd8 = 'Nov-22' AND t7.pd9 ='Nov-22' AND t7.pd10 ='Nov-22'
                    AND t8.pd1 = 'Apr-23' AND t8.pd2 = 'Apr-23' AND t8.pd3 = 'Apr-23' AND t8.pd4 ='Apr-23';"""
            cur.execute(query)
            results.extend(cur.fetchall())
            return render_template('Gallery.html', results=results)

        elif query_type == 'list_students_with_backlogs':
            query = """ SELECT t1.regdno,t1.name AS name_table1,
                              SUM(
                                  CASE WHEN t1.pd1 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t1.pd2 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t1.pd3 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t1.pd4 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t1.pd5 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t1.pd6 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t1.pd7 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t1.pd8 = '-' THEN 1 ELSE 0 END
                              ) AS backlog_count_t1,
                              SUM(
                                  CASE WHEN t2.pd1 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t2.pd2 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t2.pd3 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t2.pd4 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t2.pd5 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t2.pd6 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t2.pd7 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t2.pd8 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t2.pd9 = '-' THEN 1 ELSE 0 END
                              ) AS backlog_count_t2,
                              SUM(
                                  CASE WHEN t3.pd1 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t3.pd2 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t3.pd3 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t3.pd4 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t3.pd5 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t3.pd6 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t3.pd7 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t3.pd8 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t3.pd9 = '-' THEN 1 ELSE 0 END
                              ) AS backlog_count_t3,
                              SUM(
                                  CASE WHEN t4.pd1 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t4.pd2 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t4.pd3 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t4.pd4 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t4.pd5 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t4.pd6 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t4.pd7 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t4.pd8 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t4.pd9 = '-' THEN 1 ELSE 0 END
                              ) AS backlog_count_t4,
                              SUM(
                                  CASE WHEN t5.pd1 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t5.pd2 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t5.pd3 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t5.pd4 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t5.pd5 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t5.pd6 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t5.pd7 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t5.pd8 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t5.pd9 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t5.pd10 = '-' THEN 1 ELSE 0 END
                              ) AS backlog_count_t5,
                              SUM(
                                  CASE WHEN t6.pd1 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t6.pd2 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t6.pd3 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t6.pd4 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t6.pd5 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t6.pd6 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t6.pd7 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t6.pd8 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t6.pd9 = '-' THEN 1 ELSE 0 END
                              ) AS backlog_count_t6,
                              SUM(
                                  CASE WHEN t7.pd1 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t7.pd2 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t7.pd3 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t7.pd4 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t7.pd5 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t7.pd6 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t7.pd7 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t7.pd8 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t7.pd9 = '-' THEN 1 ELSE 0 END +
		                          CASE WHEN t7.pd10 = '-' THEN 1 ELSE 0 END
                              ) AS backlog_count_t7,
                              SUM(
                                  CASE WHEN t8.pd1 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t8.pd2 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t8.pd3 = '-' THEN 1 ELSE 0 END +
                                  CASE WHEN t8.pd4 = '-' THEN 1 ELSE 0 END 
                              ) AS backlog_count_t8,
                               SUM(
                                   CASE WHEN t1.pd1 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t1.pd2 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t1.pd3 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t1.pd4 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t1.pd5 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t1.pd6 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t1.pd7 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t1.pd8 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t2.pd1 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t2.pd2 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t2.pd3 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t2.pd4 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t2.pd5 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t2.pd6 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t2.pd7 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t2.pd8 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t2.pd9 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t3.pd1 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t3.pd2 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t3.pd3 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t3.pd4 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t3.pd5 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t3.pd6 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t3.pd7 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t3.pd8 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t3.pd9 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t4.pd1 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t4.pd2 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t4.pd3 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t4.pd4 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t4.pd5 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t4.pd6 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t4.pd7 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t4.pd8 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t4.pd9 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t5.pd1 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t5.pd2 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t5.pd3 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t5.pd4 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t5.pd5 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t5.pd6 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t5.pd7 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t5.pd8 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t5.pd9 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t5.pd10 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t6.pd1 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t6.pd2 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t6.pd3 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t6.pd4 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t6.pd5 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t6.pd6 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t6.pd7 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t6.pd8 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t6.pd9 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t7.pd1 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t7.pd2 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t7.pd3 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t7.pd4 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t7.pd5 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t7.pd6 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t7.pd7 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t7.pd8 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t7.pd9 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t7.pd10 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t8.pd1 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t8.pd2 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t8.pd3 = '-' THEN 1 ELSE 0 END +
                                   CASE WHEN t8.pd4 = '-' THEN 1 ELSE 0 END
                               ) AS total_backlog_sum
                                FROM 
                                r18s11 t1
                                JOIN 
                                   r18s12 t2 ON t1.regdno = t2.regdno
                                JOIN 
                                    r18s21 t3 ON t1.regdno = t3.regdno
                                JOIN 
                                     r18s22 t4 ON t3.regdno = t4.regdno
                                JOIN 
                                    r18s31 t5 ON t4.regdno = t5.regdno
                                JOIN 
                                    r18s32 t6 ON t5.regdno = t6.regdno
                                JOIN 
                                    r18s41 t7 ON t6.regdno = t7.regdno
                                JOIN 
                                    r18s42 t8 ON t7.regdno = t8.regdno
                                WHERE 
                                   t1.pd1 = '-' OR t1.pd2 = '-' OR t1.pd3 = '-' OR t1.pd4 = '-' OR t1.pd5 = '-' OR t1.pd6 = '-' OR t1.pd7 = '-' OR t1.pd8 = '-' OR
                                    t2.pd1 = '-' OR t2.pd2 = '-' OR t2.pd3 = '-' OR t2.pd4 = '-' OR t2.pd5 = '-' OR t2.pd6 = '-' OR t2.pd7 = '-' OR t2.pd8 = '-' OR t2.pd9 = '-' OR
                                   t3.pd1 = '-' OR t3.pd2 = '-' OR t3.pd3 = '-' OR t3.pd4 = '-' OR t3.pd5 = '-' OR t3.pd6 = '-' OR t3.pd7 = '-' OR t3.pd8 = '-' OR t3.pd9 = '-' OR
                                   t4.pd1 = '-' OR t4.pd2 = '-' OR t4.pd3 = '-' OR t4.pd4 = '-' OR t4.pd5 = '-' OR t4.pd6 = '-' OR t4.pd7 = '-' OR t4.pd8 = '-' OR t4.pd9 = '-' OR
                                   t5.pd1 = '-' OR t5.pd2 = '-' OR t5.pd3 = '-' OR t5.pd4 = '-' OR t5.pd5 = '-' OR t5.pd6 = '-' OR t5.pd7 = '-' OR t5.pd8 = '-' OR t5.pd9 = '-' OR t5.pd10 = '-' OR
                                   t6.pd1 = '-' OR t6.pd2 = '-' OR t6.pd3 = '-' OR t6.pd4 = '-' OR t6.pd5 = '-' OR t6.pd6 = '-' OR t6.pd7 = '-' OR t6.pd8 = '-' OR t6.pd9 = '-' OR
                                   t7.pd1 = '-' OR t7.pd2 = '-' OR t7.pd3 = '-' OR t7.pd4 = '-' OR t7.pd5 = '-' OR t7.pd6 = '-' OR t7.pd7 = '-' OR t7.pd8 = '-' OR t7.pd9 = '-' OR t7.pd10 = '-' OR
                                   t8.pd1 = '-' OR t8.pd2 = '-' OR t8.pd3 = '-' OR t8.pd4 = '-'
                                GROUP BY 
                                 t1.regdno, 
                                  t1.name
                                LIMIT 1000;"""
            cur.execute(query)
            results11.extend(cur.fetchall())
            return render_template('y19backlogs.html', results11=results11)
        elif query_type == "negative_trend_backlogs":
            query = """ SELECT * FROM (
                                SELECT t1.regdno,t1.name AS name_table1,
                                SUM(
                                          CASE WHEN t1.pd1 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t1.pd2 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t1.pd3 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t1.pd4 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t1.pd5 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t1.pd6 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t1.pd7 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t1.pd8 = '-' THEN 1 ELSE 0 END
                                      ) AS backlog_count_t1,
                                      SUM(
                                          CASE WHEN t2.pd1 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t2.pd2 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t2.pd3 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t2.pd4 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t2.pd5 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t2.pd6 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t2.pd7 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t2.pd8 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t2.pd9 = '-' THEN 1 ELSE 0 END
                                      ) AS backlog_count_t2,
                                      SUM(
                                          CASE WHEN t3.pd1 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t3.pd2 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t3.pd3 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t3.pd4 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t3.pd5 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t3.pd6 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t3.pd7 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t3.pd8 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t3.pd9 = '-' THEN 1 ELSE 0 END
                                      ) AS backlog_count_t3,
                                      SUM(
                                          CASE WHEN t4.pd1 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t4.pd2 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t4.pd3 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t4.pd4 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t4.pd5 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t4.pd6 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t4.pd7 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t4.pd8 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t4.pd9 = '-' THEN 1 ELSE 0 END
                                      ) AS backlog_count_t4,
                                      SUM(
                                          CASE WHEN t5.pd1 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t5.pd2 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t5.pd3 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t5.pd4 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t5.pd5 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t5.pd6 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t5.pd7 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t5.pd8 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t5.pd9 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t5.pd10 = '-' THEN 1 ELSE 0 END
                                      ) AS backlog_count_t5,
                                      SUM(
                                          CASE WHEN t6.pd1 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t6.pd2 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t6.pd3 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t6.pd4 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t6.pd5 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t6.pd6 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t6.pd7 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t6.pd8 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t6.pd9 = '-' THEN 1 ELSE 0 END
                                      ) AS backlog_count_t6,
                                      SUM(
                                          CASE WHEN t7.pd1 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t7.pd2 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t7.pd3 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t7.pd4 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t7.pd5 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t7.pd6 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t7.pd7 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t7.pd8 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t7.pd9 = '-' THEN 1 ELSE 0 END +
        		                          CASE WHEN t7.pd10 = '-' THEN 1 ELSE 0 END
                                      ) AS backlog_count_t7,
                                      SUM(
                                          CASE WHEN t8.pd1 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t8.pd2 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t8.pd3 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t8.pd4 = '-' THEN 1 ELSE 0 END 
                                      ) AS backlog_count_t8,
                                       SUM(
                                           CASE WHEN t1.pd1 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t1.pd2 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t1.pd3 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t1.pd4 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t1.pd5 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t1.pd6 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t1.pd7 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t1.pd8 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t2.pd1 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t2.pd2 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t2.pd3 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t2.pd4 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t2.pd5 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t2.pd6 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t2.pd7 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t2.pd8 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t2.pd9 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t3.pd1 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t3.pd2 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t3.pd3 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t3.pd4 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t3.pd5 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t3.pd6 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t3.pd7 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t3.pd8 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t3.pd9 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t4.pd1 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t4.pd2 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t4.pd3 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t4.pd4 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t4.pd5 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t4.pd6 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t4.pd7 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t4.pd8 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t4.pd9 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t5.pd1 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t5.pd2 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t5.pd3 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t5.pd4 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t5.pd5 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t5.pd6 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t5.pd7 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t5.pd8 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t5.pd9 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t5.pd10 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t6.pd1 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t6.pd2 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t6.pd3 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t6.pd4 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t6.pd5 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t6.pd6 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t6.pd7 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t6.pd8 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t6.pd9 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t7.pd1 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t7.pd2 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t7.pd3 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t7.pd4 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t7.pd5 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t7.pd6 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t7.pd7 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t7.pd8 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t7.pd9 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t7.pd10 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t8.pd1 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t8.pd2 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t8.pd3 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t8.pd4 = '-' THEN 1 ELSE 0 END
                                       ) AS total_backlog_sum
                                        FROM 
                                        r18s11 t1
                                        JOIN 
                                           r18s12 t2 ON t1.regdno = t2.regdno
                                        JOIN 
                                            r18s21 t3 ON t1.regdno = t3.regdno
                                        JOIN 
                                             r18s22 t4 ON t3.regdno = t4.regdno
                                        JOIN 
                                            r18s31 t5 ON t4.regdno = t5.regdno
                                        JOIN 
                                            r18s32 t6 ON t5.regdno = t6.regdno
                                        JOIN 
                                            r18s41 t7 ON t6.regdno = t7.regdno
                                        JOIN 
                                            r18s42 t8 ON t7.regdno = t8.regdno
                                        WHERE 
                                           t1.pd1 = '-' OR t1.pd2 = '-' OR t1.pd3 = '-' OR t1.pd4 = '-' OR t1.pd5 = '-' OR t1.pd6 = '-' OR t1.pd7 = '-' OR t1.pd8 = '-' OR
                                            t2.pd1 = '-' OR t2.pd2 = '-' OR t2.pd3 = '-' OR t2.pd4 = '-' OR t2.pd5 = '-' OR t2.pd6 = '-' OR t2.pd7 = '-' OR t2.pd8 = '-' OR t2.pd9 = '-' OR
                                           t3.pd1 = '-' OR t3.pd2 = '-' OR t3.pd3 = '-' OR t3.pd4 = '-' OR t3.pd5 = '-' OR t3.pd6 = '-' OR t3.pd7 = '-' OR t3.pd8 = '-' OR t3.pd9 = '-' OR
                                           t4.pd1 = '-' OR t4.pd2 = '-' OR t4.pd3 = '-' OR t4.pd4 = '-' OR t4.pd5 = '-' OR t4.pd6 = '-' OR t4.pd7 = '-' OR t4.pd8 = '-' OR t4.pd9 = '-' OR
                                           t5.pd1 = '-' OR t5.pd2 = '-' OR t5.pd3 = '-' OR t5.pd4 = '-' OR t5.pd5 = '-' OR t5.pd6 = '-' OR t5.pd7 = '-' OR t5.pd8 = '-' OR t5.pd9 = '-' OR t5.pd10 = '-' OR
                                           t6.pd1 = '-' OR t6.pd2 = '-' OR t6.pd3 = '-' OR t6.pd4 = '-' OR t6.pd5 = '-' OR t6.pd6 = '-' OR t6.pd7 = '-' OR t6.pd8 = '-' OR t6.pd9 = '-' OR
                                           t7.pd1 = '-' OR t7.pd2 = '-' OR t7.pd3 = '-' OR t7.pd4 = '-' OR t7.pd5 = '-' OR t7.pd6 = '-' OR t7.pd7 = '-' OR t7.pd8 = '-' OR t7.pd9 = '-' OR t7.pd10 = '-' OR
                                           t8.pd1 = '-' OR t8.pd2 = '-' OR t8.pd3 = '-' OR t8.pd4 = '-'
                                        GROUP BY 
                                         t1.regdno,t1.name
                                        ) AS subquery
                                        WHERE 
                                        backlog_count_t1 > backlog_count_t2 AND backlog_count_t2 > backlog_count_t3 AND
                                        backlog_count_t3 > backlog_count_t4 AND backlog_count_t4 > backlog_count_t5 AND
                                        backlog_count_t5 > backlog_count_t6 AND backlog_count_t6 > backlog_count_t7 AND
                                        backlog_count_t7 > backlog_count_t8 
                                        ORDER BY total_backlog_sum; """
            cur.execute(query)
            results2.extend(cur.fetchall())
            return render_template('backlogs negative trend.html', results2=results2)

        elif query_type == "negative_trend_backlogs":
            query = """ SELECT * FROM (
                                SELECT t1.regdno,t1.name AS name_table1,
                                SUM(
                                          CASE WHEN t1.pd1 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t1.pd2 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t1.pd3 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t1.pd4 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t1.pd5 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t1.pd6 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t1.pd7 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t1.pd8 = '-' THEN 1 ELSE 0 END
                                      ) AS backlog_count_t1,
                                      SUM(
                                          CASE WHEN t2.pd1 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t2.pd2 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t2.pd3 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t2.pd4 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t2.pd5 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t2.pd6 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t2.pd7 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t2.pd8 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t2.pd9 = '-' THEN 1 ELSE 0 END
                                      ) AS backlog_count_t2,
                                      SUM(
                                          CASE WHEN t3.pd1 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t3.pd2 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t3.pd3 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t3.pd4 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t3.pd5 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t3.pd6 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t3.pd7 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t3.pd8 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t3.pd9 = '-' THEN 1 ELSE 0 END
                                      ) AS backlog_count_t3,
                                      SUM(
                                          CASE WHEN t4.pd1 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t4.pd2 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t4.pd3 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t4.pd4 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t4.pd5 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t4.pd6 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t4.pd7 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t4.pd8 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t4.pd9 = '-' THEN 1 ELSE 0 END
                                      ) AS backlog_count_t4,
                                      SUM(
                                          CASE WHEN t5.pd1 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t5.pd2 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t5.pd3 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t5.pd4 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t5.pd5 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t5.pd6 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t5.pd7 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t5.pd8 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t5.pd9 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t5.pd10 = '-' THEN 1 ELSE 0 END
                                      ) AS backlog_count_t5,
                                      SUM(
                                          CASE WHEN t6.pd1 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t6.pd2 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t6.pd3 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t6.pd4 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t6.pd5 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t6.pd6 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t6.pd7 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t6.pd8 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t6.pd9 = '-' THEN 1 ELSE 0 END
                                      ) AS backlog_count_t6,
                                      SUM(
                                          CASE WHEN t7.pd1 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t7.pd2 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t7.pd3 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t7.pd4 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t7.pd5 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t7.pd6 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t7.pd7 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t7.pd8 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t7.pd9 = '-' THEN 1 ELSE 0 END +
        		                          CASE WHEN t7.pd10 = '-' THEN 1 ELSE 0 END
                                      ) AS backlog_count_t7,
                                      SUM(
                                          CASE WHEN t8.pd1 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t8.pd2 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t8.pd3 = '-' THEN 1 ELSE 0 END +
                                          CASE WHEN t8.pd4 = '-' THEN 1 ELSE 0 END 
                                      ) AS backlog_count_t8,
                                       SUM(
                                           CASE WHEN t1.pd1 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t1.pd2 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t1.pd3 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t1.pd4 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t1.pd5 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t1.pd6 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t1.pd7 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t1.pd8 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t2.pd1 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t2.pd2 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t2.pd3 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t2.pd4 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t2.pd5 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t2.pd6 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t2.pd7 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t2.pd8 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t2.pd9 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t3.pd1 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t3.pd2 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t3.pd3 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t3.pd4 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t3.pd5 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t3.pd6 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t3.pd7 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t3.pd8 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t3.pd9 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t4.pd1 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t4.pd2 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t4.pd3 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t4.pd4 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t4.pd5 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t4.pd6 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t4.pd7 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t4.pd8 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t4.pd9 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t5.pd1 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t5.pd2 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t5.pd3 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t5.pd4 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t5.pd5 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t5.pd6 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t5.pd7 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t5.pd8 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t5.pd9 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t5.pd10 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t6.pd1 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t6.pd2 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t6.pd3 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t6.pd4 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t6.pd5 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t6.pd6 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t6.pd7 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t6.pd8 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t6.pd9 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t7.pd1 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t7.pd2 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t7.pd3 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t7.pd4 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t7.pd5 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t7.pd6 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t7.pd7 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t7.pd8 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t7.pd9 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t7.pd10 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t8.pd1 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t8.pd2 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t8.pd3 = '-' THEN 1 ELSE 0 END +
                                           CASE WHEN t8.pd4 = '-' THEN 1 ELSE 0 END
                                       ) AS total_backlog_sum
                                        FROM 
                                        r18s11 t1
                                        JOIN 
                                           r18s12 t2 ON t1.regdno = t2.regdno
                                        JOIN 
                                            r18s21 t3 ON t1.regdno = t3.regdno
                                        JOIN 
                                             r18s22 t4 ON t3.regdno = t4.regdno
                                        JOIN 
                                            r18s31 t5 ON t4.regdno = t5.regdno
                                        JOIN 
                                            r18s32 t6 ON t5.regdno = t6.regdno
                                        JOIN 
                                            r18s41 t7 ON t6.regdno = t7.regdno
                                        JOIN 
                                            r18s42 t8 ON t7.regdno = t8.regdno
                                        WHERE 
                                           t1.pd1 = '-' OR t1.pd2 = '-' OR t1.pd3 = '-' OR t1.pd4 = '-' OR t1.pd5 = '-' OR t1.pd6 = '-' OR t1.pd7 = '-' OR t1.pd8 = '-' OR
                                            t2.pd1 = '-' OR t2.pd2 = '-' OR t2.pd3 = '-' OR t2.pd4 = '-' OR t2.pd5 = '-' OR t2.pd6 = '-' OR t2.pd7 = '-' OR t2.pd8 = '-' OR t2.pd9 = '-' OR
                                           t3.pd1 = '-' OR t3.pd2 = '-' OR t3.pd3 = '-' OR t3.pd4 = '-' OR t3.pd5 = '-' OR t3.pd6 = '-' OR t3.pd7 = '-' OR t3.pd8 = '-' OR t3.pd9 = '-' OR
                                           t4.pd1 = '-' OR t4.pd2 = '-' OR t4.pd3 = '-' OR t4.pd4 = '-' OR t4.pd5 = '-' OR t4.pd6 = '-' OR t4.pd7 = '-' OR t4.pd8 = '-' OR t4.pd9 = '-' OR
                                           t5.pd1 = '-' OR t5.pd2 = '-' OR t5.pd3 = '-' OR t5.pd4 = '-' OR t5.pd5 = '-' OR t5.pd6 = '-' OR t5.pd7 = '-' OR t5.pd8 = '-' OR t5.pd9 = '-' OR t5.pd10 = '-' OR
                                           t6.pd1 = '-' OR t6.pd2 = '-' OR t6.pd3 = '-' OR t6.pd4 = '-' OR t6.pd5 = '-' OR t6.pd6 = '-' OR t6.pd7 = '-' OR t6.pd8 = '-' OR t6.pd9 = '-' OR
                                           t7.pd1 = '-' OR t7.pd2 = '-' OR t7.pd3 = '-' OR t7.pd4 = '-' OR t7.pd5 = '-' OR t7.pd6 = '-' OR t7.pd7 = '-' OR t7.pd8 = '-' OR t7.pd9 = '-' OR t7.pd10 = '-' OR
                                           t8.pd1 = '-' OR t8.pd2 = '-' OR t8.pd3 = '-' OR t8.pd4 = '-'
                                        GROUP BY 
                                         t1.regdno,t1.name
                                        ) AS subquery
                                        WHERE 
                                        backlog_count_t1 <= backlog_count_t2 AND backlog_count_t2 <= backlog_count_t3 AND
                                        backlog_count_t3 <= backlog_count_t4 AND backlog_count_t4 <= backlog_count_t5 AND
                                        backlog_count_t5 <= backlog_count_t6 AND backlog_count_t6 <= backlog_count_t7 AND
                                        backlog_count_t7 <= backlog_count_t8 
                                        ORDER BY total_backlog_sum; """
            cur.execute(query)
            results33.extend(cur.fetchall())
            return render_template('y19backlogs negative trend.html', results33=results33)


if __name__ == '__main__':
    app.run(debug=True)
