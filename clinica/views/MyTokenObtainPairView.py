from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # Adiciona o nome do usuário no retorno do JSON
        data['username'] = self.user.username
        # Se você tiver um campo 'nome_completo' no model, pode usar:
        # data['nome'] = self.user.first_name 
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer