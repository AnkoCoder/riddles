from app import db, Riddle

db.drop_all()
db.create_all()

riddles = []
riddles.append(Riddle(
    question='В Полотняной стране по реке простыне плывет пароход. То назад, то вперед. А за ним такая гладь — ни морщинки не видать.', 
    answer='Утюг'
    ))
riddles.append(Riddle(
    question='В брюшке — баня, в носу — решето, нос — хоботок, на голове — пупок, сего одна рука без пальчиков, и та — на спине калачиком.', 
    answer='Чайник'
    ))
riddles.append(Riddle(
    question='Речка спятила с ума — по домам пошла сама.', 
    answer='Водопровод'
    ))
riddles.append(Riddle(
    question='На раскрашенных страницах много праздников хранится.', 
    answer='Календарь'
    ))

for riddle in riddles:
    db.session.add(riddle)

db.session.commit()