
# days 2

total_bill=int(input("Enter your total bill\n"))
total_tip_persentage=int(input("Enter tipp percentage\n"))
how_many=int(input('How many pepole with you\n'))

total_amount_per_person=(((total_bill/100) * total_tip_persentage ) + total_bill)/how_many
# get_pasentage_of_tipp= total_bill/100 * total_tip_persentage
# bill_with_tipp =total_bill + get_pasentage_of_tipp
# final_bill=bill_with_tipp/how_many
round_it=round(total_amount_per_person,2)
print(f"Total bill per person {round_it}")