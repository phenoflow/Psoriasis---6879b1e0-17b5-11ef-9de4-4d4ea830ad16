# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"M161z00","system":"readv2"},{"code":"M161000","system":"readv2"},{"code":"M161E00","system":"readv2"},{"code":"M161600","system":"readv2"},{"code":"M161B00","system":"readv2"},{"code":"14F2.00","system":"readv2"},{"code":"M161J00","system":"readv2"},{"code":"M161F11","system":"readv2"},{"code":"M161H00","system":"readv2"},{"code":"M16y000","system":"readv2"},{"code":"M161700","system":"readv2"},{"code":"M161500","system":"readv2"},{"code":"M161200","system":"readv2"},{"code":"M161100","system":"readv2"},{"code":"M161900","system":"readv2"},{"code":"M161F00","system":"readv2"},{"code":"M161800","system":"readv2"},{"code":"M160000","system":"readv2"},{"code":"M161300","system":"readv2"},{"code":"M161400","system":"readv2"},{"code":"M161A00","system":"readv2"},{"code":"M161C00","system":"readv2"},{"code":"8014.0","system":"readv2"},{"code":"21633.0","system":"readv2"},{"code":"105229.0","system":"readv2"},{"code":"41149.0","system":"readv2"},{"code":"3437.0","system":"readv2"},{"code":"3193.0","system":"readv2"},{"code":"4231.0","system":"readv2"},{"code":"30272.0","system":"readv2"},{"code":"162.0","system":"readv2"},{"code":"59107.0","system":"readv2"},{"code":"21503.0","system":"readv2"},{"code":"28456.0","system":"readv2"},{"code":"11761.0","system":"readv2"},{"code":"30975.0","system":"readv2"},{"code":"17094.0","system":"readv2"},{"code":"93511.0","system":"readv2"},{"code":"2945.0","system":"readv2"},{"code":"30210.0","system":"readv2"},{"code":"96880.0","system":"readv2"},{"code":"60169.0","system":"readv2"},{"code":"172.0","system":"readv2"},{"code":"48257.0","system":"readv2"},{"code":"20222.0","system":"readv2"},{"code":"42008.0","system":"readv2"},{"code":"3733.0","system":"readv2"},{"code":"22501.0","system":"readv2"},{"code":"18755.0","system":"readv2"},{"code":"66711.0","system":"readv2"},{"code":"24136.0","system":"readv2"},{"code":"21104.0","system":"readv2"},{"code":"65839.0","system":"readv2"},{"code":"12500.0","system":"readv2"},{"code":"476.0","system":"readv2"},{"code":"26368.0","system":"readv2"},{"code":"107494.0","system":"readv2"},{"code":"32149.0","system":"readv2"},{"code":"L40","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('psoriasis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["psoriasis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["psoriasis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["psoriasis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
