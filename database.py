from datetime import datetime
import sqlite3
class Database:
    def __init__(self, database):
        self.conn = sqlite3.connect(database, check_same_thread=False)
        self.cur = self.conn.cursor()
        self.cur.execute(
            """
                CREATE TABLE IF NOT EXISTS 'ingredient' (
                'id' INTEGER NOT NULL ,
                'iname' TEXT NOT NULL,
                'ecode' TEXT NOT NULL,
                'id_status' INTEGER NOT NULL,
                'desc' TEXT NOT NULL,
                PRIMARY KEY ("id" AUTOINCREMENT)
                );

            """
        )
        self.cur.execute(
"""INSERT INTO 'ingredient' ('iname', 'ecode', 'id_status', 'desc') VALUES 
("Adipic Acid","E355",1,"A Component of fat, prepared either naturally from beet juice or synthetically.It\'s used in baking powders instead of tartar and phosphates because of it\'s hygroscopic property. Studies show that natural adipic acid is better for health in the long run."),
("Agar","E406",1,"A seaweed derivative also known as agar-agar. It\'s a gelling agent used in the preparation of jello or jelly similar to the ones prepared from collagen which is an animal derivative. Islamically, agar is far better than collagen.It is typically sold as packaged strips of washed and dried seaweed, or in powdered form."),
("Alanine","",3,"A crystalline water-soluble non-essential amino acid. Any protein-containing food such as meat, poultry, fish, eggs or dairy products is rich in alanine.Some plants also contain alanine.It is important to determine the source of alanine."),
("Albumen","",1,"Egg white is the common name for albumen. It is often separated and used for cooking (for glairs, meringues, souffl?s, and some omelettes), whence it derives its name: when albumen is beaten or cooked it turns white."),
("Albumin","",1,"A water-soluble protein coagulated by heat, found in many animal and plant tissues, especially milk, egg white, and blood plasma."),
("Alcohol (alcohol beverages)","",2,"All sorts of alcohol are strictly not permissible for consumption in Islam whether it is alot (e.g. beverages) or a bit (present in food for flavourings)."),
("Alpha Carotene (colouring)","E160a",4,"Carotene itself is halal but Glycerince may be used as the carrier. If Halal carrier is used, it is Halal."),
("Ambergris","",1,"It is a solid, waxy, flammable substance. Ambergris occurs as a biliary secretion of the intestines of the sperm whale, and can be found floating upon the sea, or in the sand near the coast. Procedures for the microbial production of ambrox have also been devised.Its been used for medicinal, flavoring purposes and important perfume odorant."),
("Amylose","",1,"It is one of the two components of starch, the other being amylopectin.Out of the two amylose is preferred for storage in plants."),
("Anatto Extracts","E160b",1,"Yellowish red dye made from the pulp enclosing the seeds of a small tropical tree, used to color fabric and food products."),
("Anchovies","",1,"Small fish.They are a key ingredient in Caesar salad and Spaghetti alla Puttanesca, and are often used as a pizza topping. Because of the strong flavor they are also an ingredient in several sauces, including Worcestershire sauce and many fish sauces."),
("Animal Fat","",4,"Animal fats are fats obtained from animal sources, including:blubber, cod liver oil, lard (pork fat), tallow (beef fat), schmaltz(chicken fat).Lard is haram in any case.As for other sources of animal fat they must come from a zabihah animal.Fish oil is also halal."),
("Animal Shortening","",4,"Shortening is a type of fat that is solid at room temperature, and is used for making many baked foods. Animal shortening, such as lard, must be avoided.Shortening from zabihah animal is halal"),
("Animal Tissue Extract","",2,"We must consider it haram if no indication or label specifying it from a halal source (zabihah animal, fish)"),
("Antioxidants","",1,"Chemical compounds used to protect certain food components from being destroyed or lost through oxidation.");"""
    )
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS 'ecode' (
            'id' INTEGER NOT NULL,
            'ecode' TEXT NOT NULL,
            'iname' TEXT NOT NULL,
            'category' TEXT NOT NULL,
            'id_status' INTEGER NOT NULL,
            'desc' TEXT NOT NULL,
            PRIMARY KEY ("id" AUTOINCREMENT)
            );
            """

        )
        self.cur.execute(
            """INSERT INTO 'ecode' ('ecode','iname','category', 'id_status', 'desc') VALUES
("E100","Curcumin, turmeric","Colouring",1,"Turmeric when used as a food additive is used in product systems that are packaged to protect them from sunlight. Turmeric has found application in canned beverages, baked products, dairy products, ice cream, yogurts, yellow cakes, biscuits, popcorn-color, sweets, cake icings, cereals, sauces, gelatines, direct compression tablets, etc. Turmeric, a representative of plant genus Curcuma, is a member of the ginger family, Zingiberaceae hence halal."),
("E101","Riboflavin (Vitamin B2)","Colouring",1,"Riboflavin formerly called lactoflavin (Vitamin G) is yellow or orange-yellow in colour and in addition to being used as a food Colouring. It is also used to fortify some foods. It can be found in baby foods, breakfast cereals, sauces, processed cheese, fruit drinks and vitamin-enriched milk products as well as being widely used in vitamin supplements. Usually the source is synthetic."),
("E101a","Riboflavin-5\'-Phosphate","Colouring",1,"It is used as a food dye and is likely to be derived from genetically modified organisms."),
("E102","Tartrazine","Colouring",1,"A synthetic yellow azo dye found in fruit squash, fruit cordial, coloured fizzy drinks, instant puddings, cake mixes, custard powder, soups, sauces, ice cream, sweets, chewing gum, marzipan, jam, jelly, mustard, yoghurt and many convenience foods together with glycerine, lemon and honey products. It can also be found in the shells of medicinal capsules. It appears to cause the most allergic and/or intolerance reactions of all the azo dyes, particularly amongst those with an aspirin intolerance and asthmatics. Not recommended for consumption by children. Its use is banned in Norway and Austria."),
("E103","Chrysoine Resorcinol","Colouring",1,"It is a colourant which is used as a food additive. In Europe, it was assigned to the E number E103 until it was banned in 1984."),
("E104","Quinoline Yellow","Colouring",1,"Quinoline Yellow is a yellow/lime green dye. It is halal in its 100% dry form. In liquid form the solvent must be halal."),
("E105","Fast Yellow AB","Colouring",1,"This E-number of a food dye, is now forbidden in Europe and USA.");"""
        )
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS 'status' (
            'id' INTEGER NOT NULL,
            'status_nm' TEXT NOT NULL,
            PRIMARY KEY ("id" AUTOINCREMENT)
            );
            """
        )
        self.cur.execute(
            """INSERT INTO 'status' ('status_nm') VALUES
            ('Halal'),
            ('Haram'),
            ('Mushbooh'),
            ('Depends');"""
        )
        self.conn.commit()

    

    ##USER
    @property
    def get_time(self):
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def create_user(self,created_at, chat_id, useranme):
        self.cur.execute(
            """INSERT INTO  users(created_at, chat_id,username) VALUES (?,?,?)""",
            (created_at, chat_id, useranme)
        )
        self.conn.commit()

    def select_code(self,data):
        self.cur.execute(
            f"""SELECT a.id,a.iname,a.ecode,b.status_nm,a.desc 
                FROM ingredient a 
                LEFT JOIN status b on a.id_status=b.id 
                WHERE a.iname LIKE '{data}%' OR a.ecode='{data}'"""
        )
        return dict_fetchone(self.cur)
    
    def select_ecode(self,data):
        self.cur.execute(
            f"""SELECT a.id,a.iname,a.ecode,b.status_nm,a.desc 
                FROM ecode a 
                LEFT JOIN status b on a.id_status=b.id 
                WHERE a.ecode LIKE '{data}%'"""
        )
        return dict_fetchone(self.cur)


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))