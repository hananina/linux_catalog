from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Base, Category, Item, User
 
# engine = create_engine('sqlite:///catalog.db')
engine = create_engine( 'postgresql://catalog:catalog82205196@localhost/catalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

#User Id
user1 = User(name="hana nina", email="hananinacode@gmail.com", picture="https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png")
session.add(user1)
session.commit()

#Items for Eyes
category1 = Category(name = "Eyes", slug="eyes", user_id=user1.id)

session.add(category1)
session.commit()

item1 = Item(name = "Roller Lash Mascara", slug="roller_lash_mascara", description = "A mascara inspired by hair rollers", 
            category_id = category1.id, user_id=user1.id)

session.add(item1)
session.commit()

item2 = Item(name = "Smudge Stick Waterproof Eye Liner", slug="smudge_stick_waterproof_eye_liner", description = "Our bestselling Smudge Sticks are available in an array of matte and shimmer formulas",
             category_id = category1.id, user_id=user1.id)

session.add(item2)
session.commit()

item3 = Item(name = "Naked Eye Color Palette", slug="naked_eye_color_palette", description = "brown and dark brown",
            category_id = category1.id, user_id=user1.id)

session.add(item3)
session.commit()

item4 = Item(name = "Eye Cream", slug="eye_cream", description = "This Eye cream provides concentrated hydration for a radiantly refreshed complexion. Our exclusive tri-radiance complex helps develop the skin's water reserves and reinforces the moisture barrier. Contains mango butter, a natural plant-based emollient known to provide moisture.",
          category_id = category1.id, user_id=user1.id)

session.add(item4)
session.commit()


#Items for Lips
category2 = Category(name = "Lips", slug="lips", user_id=user1.id)

session.add(category2)
session.commit()

item1 = Item(name = "Sugar Lip Treatment Sunscreen", slug="sugar_lip_treatment_sunscreen", description = "A bestselling lip treatment and a cult favorite among all who try it, including Hollywoods elite that moisturizes, protects, and smooths the lips.",
              category_id = category2.id, user_id=user1.id)

session.add(item1)
session.commit()

item2 = Item(name = "Smashbox Always On Matte Liquid Lipstick", slug="smashbox_always_on_matte_liquid_lipstick", description = "An eight-hour wear, liquid-matte lipstick with a featherweight, comfortable formula that stays put and keeps color looking as fresh and flawless as the first swipe. ",
              category_id = category2.id, user_id=user1.id)

session.add(item2)
session.commit()

item3 = Item(name = "Dior Addict Lip Glow", slug="dior_addict_lip_glow", description = "A sheer balm that enhances your natural lip color while moisturizing and protecting lips. ", 
            category_id = category2.id, user_id=user1.id)

session.add(item3)
session.commit()

item4 = Item(name = "Bite Beauty Amuse Bouche Lipstick", slug="bite_beauty_amuse_bouche_lipstick", description = "A collection of high-impact lipsticks in dimensional shades that have been handcrafted to deliver extreme moisture, soft texture, and creamy wear. ", 
             category_id = category2.id, user_id=user1.id)

session.add(item4)
session.commit()

print "added menu items!"
