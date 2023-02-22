
### thay thế
from lxml import etree

# Đọc tệp HTML cũ vào và tạo cây phân tích cú pháp
with open('output.html', 'r', encoding='utf-8', errors='ignore') as f:
    tree = etree.parse(f)

# Lấy danh sách tất cả các phần tử trong tài liệu HTML

elements = etree.tostring(tree, encoding='unicode')
# Thay đổi nội dung của từng phần tử
new_html_string = elements.replace('(*DA)', '').replace('(*DAD)', '').replace('(*/DA)', '').replace('(*/DAD)', '').replace('(*CH)', '').replace('(*/CH)', '').replace('(*ND)', '').replace('(*/ND)', '').replace('(*YC)', '').replace('(*/YC)', '').replace('(*CHD)', '').replace('(*/CHD)', '').replace('(*CHK)', '').replace('(*/CHK)', '').strip()


# Ghi tài liệu HTML mới vào tệp
with open('new_file.html', 'w', encoding='utf-8', errors='ignore') as f:
    #f.write(etree.tostring(tree, pretty_print=True, encoding='unicode'))
    f.write(new_html_string)








