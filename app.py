from ruamel.yaml import YAML
from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)
yaml = YAML()


@app.route('/')
def homepage():
    inp_fo = open("organizations.yaml").read()  # Read the Yaml File
    organizations = yaml.load(inp_fo)
    organizations = organizations['organizations']
    return render_template('index.html', organizations=organizations)


@app.route('/organizations', methods=['GET','POST'])
def new_organization():
    if request.method == 'GET':
        redirect(url_for('homepage'))
    elif request.method == 'POST':
        # Get form data
        name = request.form['name']
        description = request.form['description']
        
        # Append file data
        file_data = open("organizations.yaml").read()  # Read the Yaml File
        code = yaml.load(file_data)
        organizations = code['organizations']
        organizations_list = list(organizations)
        new_organization = {
            'name': name,
            'description': description,
            'users': []
        }
        organizations_list.append(new_organization)
        
        # Write new list to file
        code['organizations'] = organizations_list
        file_to_write = open("organizations.yaml","w") # Open the file for Write
        yaml.dump(code, file_to_write)
        file_to_write.close()
        
        # Redirect to homepage
        return redirect(url_for('homepage'))


@app.route('/organizations/<int:organization_id>', methods=['GET','POST'])
def update_organization(organization_id):
    if request.method == 'GET':
        redirect(url_for('homepage'))
    elif request.method == 'POST':
        # Get form data
        name = request.form['name']
        description = request.form['description']

        # Update file data
        file_data = open("organizations.yaml").read()  # Read the Yaml File
        code = yaml.load(file_data)

        organizations = code['organizations']
        organizations_list = list(organizations)
        organization = organizations_list[organization_id]
        organization['name'] = name
        organization['description'] = description
        
        # Write updated list to file
        code['organizations'] = organizations_list
        file_to_write = open("organizations.yaml","w") # Open the file for Write
        yaml.dump(code, file_to_write)
        file_to_write.close()
        
        # Redirect to homepage
        return redirect(url_for('homepage'))


@app.route('/organizations/<int:organization_id>/delete', methods=['POST'])
def delete_organization(organization_id):
    yaml = YAML()
    file_data = open("organizations.yaml").read()  # Read the Yaml File
    code = yaml.load(file_data)
    organizations = code['organizations']
    organizations_list = list(organizations)
    organizations_list.pop(organization_id)
    code['organizations'] = organizations_list
    file_to_write = open("organizations.yaml","w") #Open the file for Write
    yaml.dump(code, file_to_write)
    file_to_write.close()
    return redirect(url_for('homepage'))

if __name__ == '__main__':
    app.run()
