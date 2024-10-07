from ansible.module_utils.basic import AnsibleModule
import requests

def main():
    module = AnsibleModule(
        argument_spec=dict(
            hub=dict(type='str', required=True),
            user=dict(type='str', required=True),
            state=dict(type='str', choices=['present', 'absent'], default='present')
        )
    )

    hub = module.params['hub']
    user = module.params['user']
    state = module.params['state']

    # Логика для работы с API
    # Пример запроса к API для создания пользователя
    if state == 'present':
        response = requests.post(f"http://localhost:8080/api/v1/user", json={'hub': hub, 'user': user})
    else:
        response = requests.delete(f"http://localhost:8080/api/v1/user/{user}")

    if response.status_code == 200:
        module.exit_json(changed=True, msg="User created/removed successfully")
    else:
        module.fail_json(msg="Failed to create/remove user", response=response.text)

if __name__ == '__main__':
    main()