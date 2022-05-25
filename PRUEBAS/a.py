species_html = "<br><br>"
                    for n in species_list_result:
                        species_html += "<ul>" + "<li>" + " " + n + "<br>" + "</li>" + "</ul>"

for key, value in percentage_bases.items():
    bases += key + " : " + str(value[0]) + ", " + str(round(value[1], 2)) + "%" + "<br>"