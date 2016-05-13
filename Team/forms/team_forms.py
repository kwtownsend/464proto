from django.forms import ModelForm

from Team.models import Team

from django.http import Http404
import datetime


class NewTeamForm(ModelForm):
    # name = models.CharField(max_length=20, help_text='Club name')
    # description = models.CharField(max_length=180, help_text='Club description')
    # zipcode = models.CharField(max_length=5)
    # add_date = models.DateField(default=timezone.now)
    # members = models.ManyToManyField(User)
    # policies = models.ForeignKey('clubPolicies.ClubPolicy')
    class Meta:
        model = Team
        fields = ["name"]

    # _leader = None
    _first_member = None

    # def set_leader(self, current_logged_in_member):
    #     self._leader = current_logged_in_member

    # def set_policy(self, policy):
    #     self._policy = policy

    # def get_policy(self):
    #     if self._policy:
    #         return self
    #     else:
    #         return 0

    def set_owner(self, current_logged_in_member):
        self._first_member = current_logged_in_member

    def save(self, *args, **kwargs):
        # TODO: figure out why two club policies are being created
        #       for each club.
        #       Well, get_form is being called during the GET request
        #       and during the POST request. That's why there are two.
        #       The problem is, Club objects require a related ClubPolicy object.
        # if self._policy:
        # old_policy = self._policy
        # self.instance.policies = self._policy
        # old_policy.delete()
        # else:
        #     return Http404("No policies set")
        self.instance.owner = self._first_member
        # self.instance.add_date = datetime.datetime.now(
        # self.instance.player = Cities.objects.get(pk=sel)
        resp = super(NewTeamForm, self).save(*args, **kwargs)
        return resp
