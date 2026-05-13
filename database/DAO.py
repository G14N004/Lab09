from database.DB_connect import DBConnect
from model.aeroporti import Aeroporti
from model.arcoPesato import ArcoPesato


class DAO():

    @staticmethod
    def getNodi():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from airports a  """
        cursor.execute(query)
        res = []
        for row in cursor:
            res.append(Aeroporti(**row))

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getArchi(distanza,idMap):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """SELECT 
    LEAST(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID) AS vertice_1,
    GREATEST(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID) AS vertice_2,
    AVG(DISTANCE) AS peso_arco
FROM 
    flights
GROUP BY 
    LEAST(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID),
    GREATEST(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID)
HAVING 
    AVG(DISTANCE) > %s"""
        cursor.execute(query,(distanza,))
        res = []
        for row in cursor:
            res.append(ArcoPesato(idMap[row["vertice_1"]],idMap[row["vertice_2"]],row["peso_arco"]))

        cursor.close()
        conn.close()
        return res




