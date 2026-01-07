from capaLogicaNegocio.nPersona import NPersona
import streamlit as st

class PPersona:
    def __init__(self):
        self.__nPersona = NPersona()
        if 'formularioKey' not in st.session_state:
            st.session_state.formularioKey = 0
        if 'persona_seleccionada' not in st.session_state:
            st.session_state.persona_seleccionada = ''
        if 'docidentidad_sesion' not in st.session_state:
            st.session_state.docIdentidad_sesion = ''
        if 'nombre_sesion' not in st.session_state:
            st.session_state.nombre_sesion = ''
        if 'apellidopaterno_sesion' not in st.session_state:
            st.session_state.apellidopaterno_sesion = ''
        if 'apellidomaterno_sesion' not in st.session_state:
            st.session_state.apellidomaterno_sesion = ''
        if 'edad_sesion' not in st.session_state:
            st.session_state.edad_sesion = 0
        if 'gmail_sesion' not in st.session_state:
            st.session_state.gmail_sesion = ''
        if 'password_sesion' not in st.session_state:
            st.session_state.password_sesion = ''
        self.__construirInterfaz()

    def __construirInterfaz(self):
        st.title('REGISTRO')
        if st.session_state.persona_seleccionada != '':
            st.session_state.docIdentidad_sesion = st.session_state.persona_seleccionada['docidentidad']
            st.session_state.nombre_sesion = st.session_state.persona_seleccionada['nombre']
            st.session_state.apellidopaterno_sesion = st.session_state.persona_seleccionada['apellidopaterno']
            st.session_state.apellidomaterno_sesion = st.session_state.persona_seleccionada['apellidomaterno']
            st.session_state.edad_sesion = st.session_state.persona_seleccionada['edad']
            st.session_state.gmail_sesion = st.session_state.persona_seleccionada['gmail']
            st.session_state.password_sesion = st.session_state.persona_seleccionada['password']
        with st.form(f'Formulario {st.session_state.formularioKey}'):
            txtdocIdentidad = st.text_input('Documento de Identidad', value=st.session_state.docIdentidad_sesion, disabled=st.session_state.persona_seleccionada != '')
            txtNombre = st.text_input('Nombre', value=st.session_state.nombre_sesion)
            txtApellidoPaterno = st.text_input('Apellido Paterno', value=st.session_state.apellidopaterno_sesion)
            txtApellidoMaterno = st.text_input('Apellido Materno', value=st.session_state.apellidomaterno_sesion)
            txtEdad = st.number_input('Edad', min_value = 0, max_value=150, value = st.session_state.edad_sesion)
            txtGmail = st.text_input('Gmail', value=st.session_state.gmail_sesion)
            txtPassword = st.text_input('Password', value=st.session_state.password_sesion)
            if st.session_state.persona_seleccionada != '':
                btnActualizar = st.form_submit_button('Actualizar', type='primary')
                if btnActualizar:
                    persona = {
                        'nombre': txtNombre,
                        'apellidopaterno': txtApellidoPaterno,
                        'apellidomaterno': txtApellidoMaterno,
                        'edad': txtEdad,
                        'gmail': txtGmail,
                        'password': txtPassword
                    }
                    self.actualizarPersona(persona, txtdocIdentidad)
            else:
                btnguardar = st.form_submit_button('Guardar', type='primary')

                if btnguardar:
                    persona = {
                        'docidentidad': txtdocIdentidad,
                        'nombre': txtNombre,
                        'apellidopaterno': txtApellidoPaterno,
                        'apellidomaterno': txtApellidoMaterno,
                        'edad': txtEdad,
                        'gmail': txtGmail,
                        'password': txtPassword
                    }
                    self.nuevaPersona(persona)
        self.mostrarPersonas()

    def mostrarPersonas(self):
        listaPersonas = self.__nPersona.mostrarPersonas()
        col1, col2 = st.columns([10, 2])
        with col1:
            personaSeleccionada = st.dataframe(listaPersonas, selection_mode='single-row', on_select='rerun')
        
        with col2:
            if personaSeleccionada.selection.rows:
                indice_persona = personaSeleccionada.selection.rows[0]
                personaSeleccionadaIndice = listaPersonas[indice_persona]
                btnEditar = st.button('Editar')
                btnEliminar = st.button('Eliminar')

                if btnEditar:
                    st.session_state.persona_seleccionada = personaSeleccionadaIndice
                    st.rerun()

                if btnEliminar:
                    self.eliminarPersona(personaSeleccionadaIndice['docidentidad'])
                    st.rerun()

    def nuevaPersona(self, persona: dict):
        try:
            self.__nPersona.nuevaPersona(persona)
            st.toast('Registro insertado correctamente', duration='short')
            self.limpiar()
        except Exception as e:
            st.error(e)
            st.toast('Registro no Insertado', duration='short')

    def actualizarPersona(self, persona: dict, docidentidad: str):
        try:
            self.__nPersona.actualizarPersona(persona, docidentidad)
            st.toast('Registro actualizado correctamente', duration='short')
            self.limpiar()
        except Exception as e:
            st.error(e)
            st.toast('Registro no actualizado', duration='short')

    def eliminarPersona(self, docidentidad):
        try:
            self.__nPersona.eliminarPersona(docidentidad)
            st.toast('Registro eliminado correctamente', duration='short')
        except Exception as e:
            st.error(e)
            st.toast('Registro no eliminado', duration='short')
    def limpiar(self):
        st.session_state.formularioKey += 1
        st.session_state.persona_seleccionada = ''
        st.session_state.docidentidad_sesion = ''
        st.session_state.nombre_sesion = ''
        st.session_state.apellidopaterno_sesion = ''
        st.session_state.apellidomaterno_sesion = ''
        st.session_state.edad_sesion = 0
        st.session_state.gmail_sesion = ''
        st.session_state.password_sesion = ''
        st.rerun()