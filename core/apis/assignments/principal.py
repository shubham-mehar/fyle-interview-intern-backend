from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment

from .schema import AssignmentSchema, AssignmentGradeSchema, AssignmentSubmitSchema
principal_assignments_resources = Blueprint('principal_assignments_resources',__name__)

@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
def get_assignments():
    pass

@principal_assignments_resources.route('/teachers', methods=['GET'], strict_slashes=False)
def get_teachers():
    pass

@principal_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
def regrade_assignment():
    pass