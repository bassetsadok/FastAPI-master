from keycloak import KeycloakOpenID

keycloak_openid = KeycloakOpenID(server_url="http://127.0.0.1:8000/auth/",
                                 client_id="myapp",
                                 realm_name="basset",
                                 client_secret_key="")
