import pandas as pd

df = pd.read_excel('laptop.xlsx', na_values="Missing")
cleaned_model = []
inx = df.index[df['model'].isnull()].tolist()
######################### brand #################################
inds = -1
for mode in df.model:
    if (str(mode) != "nan"):
        inds += 1
    else:
        inds += 1
        if (str(mode)=="nan" and df.brand[inds] == "ALIENWARE"):
            df = df.drop(inds, axis=0)

df = df.reset_index()
######################### model ################################
for model in df.model:
    if (str(model) != "nan"):
        cleaned_model.append(model)
    else:
        for v in inx:
            name = df.model.where(df.brand == df.loc[v, "brand"]).mode()[0]
            cleaned_model.append(name)
            break;
print(cleaned_model)
######################## processor_brand ######################################
clean_processor_brand = []
for pro_brand in df.processor_brand:
    if (str(pro_brand) != "nan"):
        clean_processor_brand.append(pro_brand)
    else:
        clean_processor_brand.append(df.processor_brand.mode()[0])
print(clean_processor_brand)
##################### gnrtn ####################################
clean_gnrtn = []
for gnrt in df.processor_gnrtn:
    if (str(gnrt) == "nan"):
        clean_gnrtn.append(df.processor_gnrtn.mode()[0])
    else:
        clean_gnrtn.append(gnrt)
print(clean_gnrtn)
######################## ram_gb ######################################
clean_ram_gb = []
for ram in df.ram_gb:
    if (str(ram).endswith("GB GB")):
        clean_ram_gb.append(ram[0] + ram[1] + " GB")
    else:
        clean_ram_gb.append(ram)
print(clean_ram_gb)
#################################################################
# ------------------------------------weight----------------------------------
cleaned_weight=[]
default_weight=list(df.loc[:,'weight'].mode())[0]

for m in df.loc[:,'weight']:
    if str(m).startswith("Casual") or str(m).startswith("ThinNlight"):
        cleaned_weight.append(str(m))
    else:
        cleaned_weight.append(default_weight)
print(cleaned_weight)

# ------------------------------------warranty----------------------------------
cleaned_warranty=[]
default_warranty=df.loc[:,'warranty'].mode()
for m in df.warranty:
   if str(m)=='nan' or int(m)<0 or int(m)>2 :
        cleaned_warranty.append(int(default_warranty))
   else:
        cleaned_warranty.append(int(m))
print(cleaned_warranty)

# ------------------------------------TouchScreen----------------------------------
cleaned_Touchscreen=[]
default_Touchscreen=list(df.loc[:,'Touchscreen'].mode())[0]

for m in df.loc[:,'Touchscreen']:
    if str(m).startswith("Y") or str(m).startswith("N"):
        cleaned_Touchscreen.append(str(m))
    else:
        cleaned_Touchscreen.append(default_Touchscreen)

print(cleaned_Touchscreen)

# ------------------------------------MOffice----------------------------------
cleaned_MOffice=[]
default_MOffice=list(df.loc[:,'msoffice'].mode())[0]

for m in df.loc[:,'msoffice']:
    if str(m).startswith("Y") or str(m).startswith("N"):
        cleaned_MOffice.append(str(m))
    else:
        cleaned_MOffice.append(default_MOffice)

print(cleaned_MOffice)

# ------------------------------------old-price----------------------------------
cleaned_oldprice=[]
default_oldprice=df.loc[:,'old_price'].mean()

for m in df.old_price:
    if str(m) =='nan' or int(m) <= 0 or int(m) >130000:
        cleaned_oldprice.append(int(default_oldprice))
    else:
        cleaned_oldprice.append(int(m))
print(cleaned_oldprice)

# ------------------------------------latest_price----------------------------------
cleaned_latestPrice = []
default_latestPrice=df.loc[:,'latest_price'].mean()

for m in df.latest_price:
    if str(m) =='nan' or (int(m) <=120000 and int(m) >=0):
        cleaned_latestPrice.append(int(m))
    else:
        cleaned_latestPrice.append(default_latestPrice)

print(cleaned_latestPrice)

# ------------------------------------discount----------------------------------
cleaned_discount=[]
default_discount=df.loc[:,'discount'].mode()

for m in df.discount:
    if str(m) =='nan' or int(m) <0 or int(m) >=40:
        cleaned_discount.append(int(default_discount))
    else:
        cleaned_discount.append(int(m))
print(cleaned_discount)

# ------------------------------------starrating----------------------------------
cleaned_starrating=[]
default_starrating=df.loc[:,'star_rating'].median()

for m in df.star_rating:
    if str(m) =='nan' or float(m) <0 or float(m) >5:
        cleaned_starrating.append(float(default_starrating))
    else:
        cleaned_starrating.append(float(m))
print(cleaned_starrating)

# ------------------------------------graphic_card_gb----------------------------------
cleaned_graphic_card_gb = []

for m in df.graphic_card_gb:
    if str(m) == 'nan' or (int(m) >= -3 and int(m) <= 5):
        cleaned_graphic_card_gb.append(int(m))
    else:
        cleaned_graphic_card_gb.append(int(4))

print(cleaned_graphic_card_gb)

###################### display_size ########################################
cleaned_display_size=[]
for display in df.display_size:
    if (str(display) != "nan"):
        cleaned_display_size.append(display)
    else:
        cleaned_display_size.append(df.display_size.mode()[0])
print(cleaned_display_size)
print(len(df))
##################### cleaned_dataset #########################################
cleaned_df = pd.DataFrame({'brand':df.brand,'model':cleaned_model,'processor_brand':clean_processor_brand,'processor_name':df.processor_name,'processor_gnrtn':clean_gnrtn,
                           'ram_gb':clean_ram_gb,'ram_type':df.ram_type,'ssd':df.ssd,'hdd':df.hdd,'os':df.os,'os_bit':df.os_bit,'graphic_card_gb':cleaned_graphic_card_gb,
                           'weight':cleaned_weight,'display_size':cleaned_display_size,'warranty':cleaned_warranty,'Touchscreen':cleaned_Touchscreen,
                           'msoffice':cleaned_MOffice,'latest_price':cleaned_latestPrice,'old_price':cleaned_oldprice,'discount':cleaned_discount,
                           'star_rating':cleaned_starrating})
cleaned_df.to_csv('Cleaned_LaptopDataset.csv')
print(cleaned_df.shape)
