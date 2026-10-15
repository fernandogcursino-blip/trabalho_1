class RegraNegocioException(Exception):
    pass

class PacienteMenorDeIdadeException(RegraNegocioException):
    pass

class HorarioInvalidoException(RegraNegocioException):
    pass

class DataPagamentoInvalidaException(RegraNegocioException):
    pass