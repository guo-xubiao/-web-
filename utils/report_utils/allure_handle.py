# 封装的allure的一些操作
import allure


class AllureHandle:

    @staticmethod
    def start_allure_test(test_name):
        """
        :param test_name:
        :return:
        """
        allure.dynamic.title(test_name)

    @staticmethod
    def add_description(description):
        """
        :param description:
        :return:
        """
        allure.dynamic.description(description)

    @staticmethod
    def add_feature(feature):
        """
        :param feature:
        :return:
        """
        allure.dynamic.feature(feature)

    @staticmethod
    def add_story(story):
        """
        :param story:
        :return:
        """
        allure.dynamic.story(story)

    @staticmethod
    def add_severity(severity):
        """
        :param severity:
        :return:
        """
        allure.dynamic.severity(severity)

    @staticmethod
    def add_tag(tag):
        """
        :param tag:
        :return:
        """
        allure.dynamic.tag(tag)

    @staticmethod
    def add_issue(issue):
        """
        :param issue:
        :return:
        """
        allure.dynamic.issue(issue)

    @staticmethod
    def add_test_id(test_id):
        """
        :param test_id:
        :return:
        """
        allure.dynamic.test_id(test_id)

    @staticmethod
    def add_label(label):
        """
        :param label:
        :return:
        """
        allure.dynamic.label(label)

    @staticmethod
    def add_epic(epic):
        """
        :param epic:
        :return:
        """
        allure.dynamic.epic(epic)

    @staticmethod
    def add_feature_id(feature_id):
        """
        :param feature_id:
        :return:
        """
        allure.dynamic.feature_id(feature_id)

    @staticmethod
    def add_story_id(story_id):
        """
        :param story_id:
        :return:
        """
        allure.dynamic.story_id(story_id)

    @staticmethod
    def add_parent_suite(parent_suite):
        """
        :param parent_suite:
        :return:
        """
        allure.dynamic.parent_suite(parent_suite)

    @staticmethod
    def add_suite(suite):
        """
        :param suite:
        :return:
        """
        allure.dynamic.suite(suite)

    @staticmethod
    def add_sub_suite(sub_suite):
        """
        :param sub_suite:
        :return:
        """
        allure.dynamic.sub_suite(sub_suite)

    @staticmethod
    def add_host(host):
        """
        :param host:
        :return:
        """
        allure.dynamic.host(host)

    @staticmethod
    def add_thread(thread):
        """
        :param thread:
        :return:
        """
        allure.dynamic.thread(thread)

    #其他方法。。。