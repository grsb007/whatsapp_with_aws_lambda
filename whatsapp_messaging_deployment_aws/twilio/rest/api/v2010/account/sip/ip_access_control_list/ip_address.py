# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class IpAddressList(ListResource):
    """  """

    def __init__(self, version, account_sid, ip_access_control_list_sid):
        """
        Initialize the IpAddressList

        :param Version version: Version that contains the resource
        :param account_sid: The unique id of the Account that is responsible for this resource.
        :param ip_access_control_list_sid: The unique id of the IpAccessControlList resource that includes this resource.

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressList
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressList
        """
        super(IpAddressList, self).__init__(version)

        # Path Solution
        self._solution = {
            'account_sid': account_sid,
            'ip_access_control_list_sid': ip_access_control_list_sid,
        }
        self._uri = '/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses.json'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams IpAddressInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists IpAddressInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of IpAddressInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of IpAddressInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return IpAddressPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of IpAddressInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of IpAddressInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return IpAddressPage(self._version, response, self._solution)

    def create(self, friendly_name, ip_address, cidr_prefix_length=values.unset):
        """
        Create a new IpAddressInstance

        :param unicode friendly_name: A human readable descriptive text for this resource, up to 64 characters long.
        :param unicode ip_address: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today.
        :param unicode cidr_prefix_length: An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used.

        :returns: Newly created IpAddressInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'IpAddress': ip_address,
            'CidrPrefixLength': cidr_prefix_length,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return IpAddressInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            ip_access_control_list_sid=self._solution['ip_access_control_list_sid'],
        )

    def get(self, sid):
        """
        Constructs a IpAddressContext

        :param sid: A string that identifies the IpAddress resource to fetch

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressContext
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressContext
        """
        return IpAddressContext(
            self._version,
            account_sid=self._solution['account_sid'],
            ip_access_control_list_sid=self._solution['ip_access_control_list_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a IpAddressContext

        :param sid: A string that identifies the IpAddress resource to fetch

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressContext
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressContext
        """
        return IpAddressContext(
            self._version,
            account_sid=self._solution['account_sid'],
            ip_access_control_list_sid=self._solution['ip_access_control_list_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.IpAddressList>'


class IpAddressPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the IpAddressPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The unique id of the Account that is responsible for this resource.
        :param ip_access_control_list_sid: The unique id of the IpAccessControlList resource that includes this resource.

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressPage
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressPage
        """
        super(IpAddressPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of IpAddressInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressInstance
        """
        return IpAddressInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            ip_access_control_list_sid=self._solution['ip_access_control_list_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.IpAddressPage>'


class IpAddressContext(InstanceContext):
    """  """

    def __init__(self, version, account_sid, ip_access_control_list_sid, sid):
        """
        Initialize the IpAddressContext

        :param Version version: Version that contains the resource
        :param account_sid: The unique sid that identifies this account
        :param ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to fetch
        :param sid: A string that identifies the IpAddress resource to fetch

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressContext
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressContext
        """
        super(IpAddressContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'account_sid': account_sid,
            'ip_access_control_list_sid': ip_access_control_list_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses/{sid}.json'.format(**self._solution)

    def fetch(self):
        """
        Fetch a IpAddressInstance

        :returns: Fetched IpAddressInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return IpAddressInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            ip_access_control_list_sid=self._solution['ip_access_control_list_sid'],
            sid=self._solution['sid'],
        )

    def update(self, ip_address=values.unset, friendly_name=values.unset,
               cidr_prefix_length=values.unset):
        """
        Update the IpAddressInstance

        :param unicode ip_address: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today.
        :param unicode friendly_name: A human readable descriptive text for this resource, up to 64 characters long.
        :param unicode cidr_prefix_length: An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used.

        :returns: Updated IpAddressInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressInstance
        """
        data = values.of({
            'IpAddress': ip_address,
            'FriendlyName': friendly_name,
            'CidrPrefixLength': cidr_prefix_length,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return IpAddressInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            ip_access_control_list_sid=self._solution['ip_access_control_list_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the IpAddressInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.IpAddressContext {}>'.format(context)


class IpAddressInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, account_sid, ip_access_control_list_sid,
                 sid=None):
        """
        Initialize the IpAddressInstance

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressInstance
        """
        super(IpAddressInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'friendly_name': payload['friendly_name'],
            'ip_address': payload['ip_address'],
            'cidr_prefix_length': deserialize.integer(payload['cidr_prefix_length']),
            'ip_access_control_list_sid': payload['ip_access_control_list_sid'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'uri': payload['uri'],
        }

        # Context
        self._context = None
        self._solution = {
            'account_sid': account_sid,
            'ip_access_control_list_sid': ip_access_control_list_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: IpAddressContext for this IpAddressInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressContext
        """
        if self._context is None:
            self._context = IpAddressContext(
                self._version,
                account_sid=self._solution['account_sid'],
                ip_access_control_list_sid=self._solution['ip_access_control_list_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this resource.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The unique id of the Account that is responsible for this resource.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def friendly_name(self):
        """
        :returns: A human readable descriptive text for this resource, up to 64 characters long.
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def ip_address(self):
        """
        :returns: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today.
        :rtype: unicode
        """
        return self._properties['ip_address']

    @property
    def cidr_prefix_length(self):
        """
        :returns: An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used.
        :rtype: unicode
        """
        return self._properties['cidr_prefix_length']

    @property
    def ip_access_control_list_sid(self):
        """
        :returns: The unique id of the IpAccessControlList resource that includes this resource.
        :rtype: unicode
        """
        return self._properties['ip_access_control_list_sid']

    @property
    def date_created(self):
        """
        :returns: The date that this resource was created, given as GMT in RFC 2822 format.
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date that this resource was last updated, given as GMT in RFC 2822 format.
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def uri(self):
        """
        :returns: The URI for this resource, relative to https://api.twilio.com
        :rtype: unicode
        """
        return self._properties['uri']

    def fetch(self):
        """
        Fetch a IpAddressInstance

        :returns: Fetched IpAddressInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressInstance
        """
        return self._proxy.fetch()

    def update(self, ip_address=values.unset, friendly_name=values.unset,
               cidr_prefix_length=values.unset):
        """
        Update the IpAddressInstance

        :param unicode ip_address: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today.
        :param unicode friendly_name: A human readable descriptive text for this resource, up to 64 characters long.
        :param unicode cidr_prefix_length: An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used.

        :returns: Updated IpAddressInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressInstance
        """
        return self._proxy.update(
            ip_address=ip_address,
            friendly_name=friendly_name,
            cidr_prefix_length=cidr_prefix_length,
        )

    def delete(self):
        """
        Deletes the IpAddressInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.IpAddressInstance {}>'.format(context)
