from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, RadioField,SelectField
from wtforms.validators import Required

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    # vote=RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])
    submit = SubmitField('SUBMIT')

class PitchForm(FlaskForm):
    category_id = SelectField('Select Category', choices=[('1', 'interview'), ('2', 'promotion'), ('3', 'pick_up_lines')])
    content = TextAreaField('make a request', validators=[Required()])
    submit = SubmitField('pitch') 

class UpvoteForm(FlaskForm):
    '''
    Class to create a wtf form for upvoting a pitch
    '''
    submit = SubmitField('Upvote')

class DownvoteForm(FlaskForm):
    '''
    Class to create a wtf form for downvoting a pitch
    '''
    submit = SubmitField('Downvote')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')