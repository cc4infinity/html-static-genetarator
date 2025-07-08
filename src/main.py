from textnode import TextNode
import os
import shutil
from converter import markdown_to_html_node, extract_title

def copy_content(from_path, to_path):
    print(os.listdir(from_path))
    files = os.listdir(from_path)
    if not os.path.exists(to_path):
        os.mkdir(to_path)
    for file in files:
        if os.path.isdir(f"{from_path}/{file}"):
            if not os.path.exists(f"{to_path}/{file}"):
                os.mkdir(f"{to_path}/{file}")
            copy_content(f"{from_path}/{file}", f"{to_path}/{file}")
            continue
        shutil.copy(f"{from_path}/{file}", f"{to_path}/")

def generate_page(from_path, template_path, dest_path):
    print(f"Genaratin page from {from_path} to {dest_path} using {template_path}")
    file = open(from_path, "r")
    template_file = open(template_path, 'r')
    content = file.read()
    template_content = template_file.read()
    html_result = markdown_to_html_node(content)
    title = extract_title(content)
    result = template_content.replace('{{ Title }}', title).replace('{{ Content }}', html_result)

    destination = open(dest_path, 'x' if not os.path.exists(dest_path) else 'w')
    destination.write(result)
        
    
    file.close()
    template_file.close()

def generate_page_recursive(from_path, template_path, to_path):
    print(from_path, os.listdir(from_path))
    files = os.listdir(from_path)
    if os.path.exists(to_path):
        shutil.rmtree(f"{to_path}")
    os.mkdir(to_path)
    for file in files:
        if os.path.isdir(f"{from_path}/{file}"):
            os.mkdir(f"{to_path}/{file}")
            generate_page_recursive(f"{from_path}/{file}", template_path, f"{to_path}/{file}")
            continue
        if file.endswith('md'):
            print(f'generating html from {file} in {from_path} to {to_path}')
            generate_page(f"{from_path}/{file}", template_path, f"{to_path}/{file[:-3]}.html")
        else:
            print(f'copyiinh non html from {file} in {from_path} to {to_path}')
            shutil.copy(f"{from_path}/{file}", f"{to_path}/")

def main():
    generate_page_recursive('./content', './template.html', './public')
    copy_content('./static', './public')
    
main()
